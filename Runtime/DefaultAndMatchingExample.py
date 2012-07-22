
from Event import * 
        
class A(Component):
    def __init__(self, aName, aStayAlive):
        Component.__init__(self, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
    
    def sleep(self, aTime):
        tm = Timer(self.evQueue)
        tm.start(aTime);
        self.executeBlockingAction(
            Blocking(TimeoutExpectation(tm))
        )
    
    def behaviour(self): 
        self.log("hai")
        self.testPort.send("foo")
        self.sleep(1.0)
        self.testPort.send("blurp")
        # self.testPort.send("Foo")
        self.log("sent all")
        self.executeBlockingAction(Blocking(PortReceiveExpectation(self.testPort)))
        self.log("bai")
                
class B(Component):
    def __init__(self, aName, aStayAlive):
        Component.__init__(self, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def altstepReceiveOnTestPort(self):
        def body():
            self.log("something received on port")
        return Blocking(PortReceiveExpectation(self.testPort)).withAction(body)
        
    def behaviour(self):
        self.defaults.append(self.altstepReceiveOnTestPort())
        self.defaults.append(
            Blocking(PortReceiveExpectation(self.testPort, "blurp"))
                .withAction( lambda : self.log("blurp received on port"))
        )
    
        tm = Timer(self.evQueue)
        tm.start(3.0)
        self.log("hai")
        
        def timeoutAction():
            self.log("timeout!")
        
        self.executeBlockingAction(
            Alternative([
                Blocking(PortReceiveExpectation(self.testPort, "Foo"))
                    .withAction( lambda : self.log("received Foo")),
                Blocking(TimeoutExpectation(tm))
                    .withAction( timeoutAction )
            ])
        )
        
        self.testPort.send("Bar")
        self.log("bai")
        
        # FIXME with threading.Timer implementation we will wait for the timer thread otherwise
        tm.stop()
        
class Example(Testcase):
    def __init__(self):
        def execute(self):
            a = A("A", True)
            b = B("B", True)
            
            connect(a.testPort, b.testPort)
            
            a.start()
            b.start()
            
            a.join()
            b.join()
            
        Testcase.__init__(self, execute, Mtc, None);

c = Control()
c.execute(Example())
