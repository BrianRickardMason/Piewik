
import Queue
import threading

class EventExpectation:
    def match(self, aEvent):
        return True
    
class Action:
    """ Action interface and empty action"""
    def __init__(self):
        self.done = False
        self.callable = lambda : None

    def execute(self):
        self.done = True
        self.callable()
    
    def withAction(self, aCallable):
        self.callable = aCallable
        return self
    
    def isDone(self):
        return self.done

# class Block(Action)
        
class Blocking(Action):
    """ Blocking action interface with empty action """
    def __init__ (self, aEvExpectation):
        Action.__init__(self)
        self.expectation = aEvExpectation
        
    def applies(self, aEvent):
        if self.expectation.match(aEvent):
            return self
        return False
    
class Alternative:
    def __init__(self, aListOfActions):
        self.actionList = aListOfActions

    def applies(self, aEvent):
        for action in self.actionList:
            command = action.applies(aEvent)
            if command :
                return command
        return False
    
    def isDone(self):
        return self.anyDone()
        
    def anyDone(self):
        for action in self.actionList:
            if action.isDone() :
                return True
        return False
    
class Interleave:
    def __init__(self, aListOfActions):
        self.actionList = aListOfActions
        
    def applies(self, aEvent):
        for action in self.actionList:
            if action.isDone():
                continue
            command = action.applies(aEvent)
            if command :
                return command
        return False
                
    def isDone(self):
        return self.allDone()
        
    def allDone(self):
        for action in self.actionList:
            if not action.isDone() :
                return False
        return True
            
class Port:
    def __init__(self, aEvQ):
        self.queue = Queue.Queue()
        self.evQ = aEvQ
        self.connected = None
        
    def inject(self, aMessage):
        self.queue.put(aMessage)
        self.evQ.put(PortReceivedEvent(self, aMessage, None))
        
    def extract(self):
        self.queue.get_nowait()
        
    def connect(self, aPort):
        self.connected = aPort
        
    def send(self, aMessage):
        self.connected.inject(aMessage)

def connect(aPort1, aPort2):
    aPort1.connect(aPort2);
    aPort2.connect(aPort1);
        
class PortReceivedEvent:
    def __init__(self, aPort, aMessage, aSender = None):
        self.port = aPort
        self.message = aMessage
        self.sender = aSender
        
class PortReceiveExpectation:
    def __init__(self, aPort):
        self.port = aPort

    def match(self, aEvent):
        if isinstance(aEvent, PortReceivedEvent):
            return aEvent.port == self.port

class Timer:
    
    # TODO stop then start, read etc.

    def __init__(self, aEvQ, aTime = None):
        self.evQ = aEvQ
        
        self.time = aTime
        # self.startTime = None
        # self.stopTime = None
        self.timer = None
    
    def __del__(self):
        if self.timer :
            self.timer.cancel()
            self.timer = None
    
    def start(self, aTime = None):
        if aTime:
            self.time = aTime
        self.timer = threading.Timer(self.time, self.timeout )
        self.timer.start()
    
    def timeout(self):
        self.evQ.put(TimeoutEvent(self))
    
    def stop(self):
        self.timer.cancel()
        self.timer = None

class TimeoutEvent:
    def __init__(self, aTimer):
        self.timer = aTimer
        
class TimeoutExpectation:
    def __init__(self, aTimer):
        self.timer = aTimer

    def match(self, aEvent):
        if isinstance(aEvent, TimeoutEvent):
            return aEvent.timer == self.timer
        
            
class EventQueue:
    def __init__(self):
        self.queue = Queue.Queue()
        
    def put(self, aEvent):
        self.queue.put(aEvent)
        
    def get(self):
        return self.queue.get()
            
class Component(threading.Thread):
    def __init__(self, aName, aStayAlive):
        threading.Thread.__init__(self, None, None, aName)
        self.evQueue = EventQueue()
        self.name = aName
        self.stayAlive = aStayAlive
        self.defaults = []
        
    def executeBlockingAction(self, aAction):
        cmd = None
        repeat = True
        while repeat:
            ev  = self.evQueue.get()
            cmd = aAction.applies(ev)
            if not cmd:
                # check defaults
                dCount = len(self.defaults)
                for i in xrange(dCount-1, -1 ,-1):
                    action = self.defaults[i]
                    cmd = action.applies(ev)
                    if cmd:
                        break;
            if cmd:
                # TODO for repeat and some other stuff 
                # context passing may be needed
                cmd.execute()
                repeat = not aAction.isDone()
                # ^assumes failing on unexpected, needed for current Interleave
                # implementation. When repeat keyword is handled, can be solved
                # in a proper way.
            else :
                print("Unhandled event: " + str(ev))
    
    def log(self, aString):
        print(self.name + ": " + aString);
    
    def run(self):
        self.behaviour()
    
    def behaviour(self):
        pass
        
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

def innerFunc():
    callCallable = lambda x : x()
    x = "works"
    def test(): 
        print (x)
    callCallable(test)
    x = "still works?"
    callCallable(test)
    # f... yeah
    callCallable(lambda : None)
