
import Queue
import threading
from copy import copy

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
    def __init__(self, aPort, aMessage = None, aSender = None):
        self.port = aPort
        self.message = aMessage
        self.sender = aSender

    def tMatch(self, aTemplate, aValue):
        # TODO delegate to matcher
        return aTemplate == aValue
        
    def match(self, aEvent):
        if not isinstance(aEvent, PortReceivedEvent):
            return False
        return  aEvent.port == self.port \
            and (self.message is None or self.tMatch(self.message, aEvent.message)) \
            and (self.sender is None or self.sender == aEvent.sender)

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
            
class Verdict:
    NONE, PASS, INCONC, FAIL, ERROR = range(5)
    STRING = ['NONE', 'PASS', 'INCONC', 'FAIL', 'ERROR']
    
    def __init__(self):
        self.value = Verdict.NONE
    
    def take(self, aValue):
        if self.value < aValue: 
            self.value = aValue
        return self.value
        
    def get(self):
        return copy(self)
        
    def str(self):
        return Verdict.STRING[self.value]
            
class Component(threading.Thread):
    def __init__(self, aName, aStayAlive):
        threading.Thread.__init__(self, None, None, aName)
        self.evQueue = EventQueue()
        self.name = aName
        self.stayAlive = aStayAlive
        self.defaults = []
        self.verdict = Verdict()
        
    def setVerdict(self, aVerdict):
        self.verdict.take(aVerdict)
        
    def getVerdict(self):
        return self.verdict.get()
        
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
                # TODO for repeat and some other stuff context passing may be needed
                cmd.execute()
                repeat = not aAction.isDone()
                # ^"very blocking", does not handle "no repeat" defaults
                # When repeat keyword is handled, can be solved in a proper way.
            else :
                print("Unhandled event: " + str(ev))
    
    def log(self, aString):
        print(self.name + ": " + aString);
    
    def run(self):
        self.behaviour()
    
    def behaviour(self):
        pass

class Mtc(Component):
    def __init__(self):
        Component.__init__(self, "MTC", False)
        self.testcase = lambda : None
        
    def setTestcase(self, aTestcase):
        self.testcase = aTestcase
        
    def setParams(self, *aParams):
        self.params = aParams
        
    def run(self):
        self.testcase(self, *self.params)

class Testcase:
    def __init__(self, aFunction, aMtcType, aSystemType):
        self.mtcType = aMtcType
        self.systemType = aSystemType
        self.function = aFunction
        
class Control():
    def execute(self, aTestcase, *aParameters):
        mtc = aTestcase.mtcType()
        # system = aTestcase.systemType()
        
        mtc.setTestcase(aTestcase.function)
        mtc.setParams(*aParameters)
        
        mtc.start()
        mtc.join()
        
        # TODO incorporate PTC verdicts into final verdict
        
        print("Final verdict = " + mtc.getVerdict().str())
        
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
