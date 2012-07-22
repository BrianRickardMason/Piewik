
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
