
from Event import * 
        
class A(Component):
    def __init__(self, aContext, aName, aStayAlive):
        Component.__init__(self, aContext, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def behaviour(self): 
        self.log("hai")
        # self.testPort.send("Foo")
        self.log("sent")
        self.executeBlockingAction(Blocking(PortReceiveExpectation(self.testPort)))
        self.log("bai")
        
class B(Component):
    def __init__(self, aContext, aName, aStayAlive):
        Component.__init__(self, aContext, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def behaviour(self):
        tm = Timer(self.evQueue)
        try:
            tm.start(4.0)
            self.log("hai")
            self.setVerdict(Verdict.PASS)
            
            def timeoutAction():
                self.log("timeout!")
                self.setVerdict(Verdict.FAIL)
            
            self.executeBlockingAction(
                Alternative([
                    Blocking(PortReceiveExpectation(self.testPort))
                        .withAction( lambda : self.log("received")),
                    Blocking(TimeoutExpectation(tm))
                        .withAction( timeoutAction )
                ])
            )
            
            self.testPort.send("Bar")
            self.log("bai")
        except:
            # FIXME with threading.Timer implementation we will wait for the timer thread otherwise
            self.log("meh")
            tm.stop()
            raise
        
        # FIXME with threading.Timer implementation we will wait for the timer thread otherwise
        tm.stop()
        
class Example(Testcase):
    def __init__(self):
        def execute(self):
            a = A(self.createContext(), "A", True)
            b = B(self.createContext(), "B", True)
            
            connect(a.testPort, b.testPort)
            
            a.start()
            b.start()
            
            b.stop()
            a.stop()
            
            a.join()
            b.join()
            
        Testcase.__init__(self, execute, Mtc, None);

c = Control()
c.execute(Example())
