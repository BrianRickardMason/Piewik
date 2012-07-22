
from Event import * 
        
class A(Component):
    def __init__(self, aContext, aName, aStayAlive):
        Component.__init__(self, aContext, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def behaviour(self): 
        self.log("hai")
        self.testPort.send("Foo")
        self.log("sent")
        self.executeBlockingAction(Blocking(PortReceiveExpectation(self.testPort)))
        self.log("bai")
        
        self.setVerdict(Verdict.PASS)
        
class B(Component):
    def __init__(self, aContext, aName, aStayAlive):
        Component.__init__(self, aContext, aName, aStayAlive)
        self.testPort = Port(self.evQueue)
        
    def behaviour(self):
        self.log("hai")
        self.executeBlockingAction(Blocking(PortReceiveExpectation(self.testPort)))
        self.log("received")
        self.testPort.send("Bar")
        self.log("bai")
        
        self.setVerdict(Verdict.PASS)
        
class Example(Testcase):
    def __init__(self):
        def execute(self):
            a = A(self.createContext(), "A", True)
            b = B(self.createContext(), "B", True)
            
            connect(a.testPort, b.testPort)
            
            a.start()
            self.log("A started")
            b.start()
            self.log("B started")
            
            # a.join()
            self.executeBlockingAction(Blocking(ComponentDoneExpectation(a)))
            self.log("A finished")
            # b.join()
            self.executeBlockingAction(Blocking(ComponentDoneExpectation(b)))
            self.log("B finished")
            
            self.executeBlockingAction(Blocking(ComponentDoneExpectation(a)))
            
        Testcase.__init__(self, execute, Mtc, None);

c = Control()
c.execute(Example())
