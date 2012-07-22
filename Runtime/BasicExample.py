
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
        self.log("hai")
        self.executeBlockingAction(Blocking(PortReceiveExpectation(self.testPort)))
        self.log("received")
        self.testPort.send("Bar")
        self.log("bai")
        
class Example(Testcase):
    def __init__(self):
        def execute(self):
            a = A("A", True)
            b = B("B", True)
            
            connect(a.testPort, b.testPort)
            
            self.setVerdict(Verdict.PASS)
            
            a.start()
            self.log("A started")
            b.start()
            self.log("B started")
            
            a.join()
            self.log("A finished")
            b.join()
            self.log("B finished")
            
        Testcase.__init__(self, execute, Mtc, None);

c = Control()
c.execute(Example())
