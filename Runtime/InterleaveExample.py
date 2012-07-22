
from Event import * 
        
class A(Component):
    def __init__(self, aName, aStayAlive):
        Component.__init__(self, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def behaviour(self): 
        self.log("hai")
        self.testPort.send("Foo")
        self.log("sent")
        self.executeBlockingAction(Blocking(PortReceiveExpectation(self.testPort)))
        self.log("bai")
        
class B(Component):
    def __init__(self, aName, aStayAlive):
        Component.__init__(self, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def behaviour(self):
        tm = Timer(self.evQueue)
        tm.start(3.0)
        self.log("hai")
        self.executeBlockingAction(
            Interleave([
                Blocking(PortReceiveExpectation(self.testPort))
                    .withAction( lambda : self.log("received")),
                Blocking(TimeoutExpectation(tm))
                    .withAction( lambda : self.log("timeout!"))
            ])
        )
        
        self.testPort.send("Bar")
        self.log("bai")
        
        # FIXME with threading.Timer implementation we will wait for the timer thread otherwise
        tm.stop()
        
class Example:
    def execute(self):
        a = A("A", True)
        b = B("B", True)
        
        connect(a.testPort, b.testPort)
        
        a.start()
        b.start()
        
        a.join()
        b.join()

        
ex = Example()
ex.execute()
