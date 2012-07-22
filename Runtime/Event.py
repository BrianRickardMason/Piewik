
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
        
    def empty(self):
        return self.queue.empty()
            
class Verdict:
    NONE, PASS, INCONC, FAIL, ERROR = range(5)
    STRING = ['NONE', 'PASS', 'INCONC', 'FAIL', 'ERROR']
    
    def __init__(self):
        self.value = Verdict.NONE
    
    def take(self, aValue):
        if self.value < aValue: 
            self.value = aValue
        return self.value
        
    def getValue(self):
        return self.value
        
    def get(self):
        return copy(self)
        
    def str(self):
        return Verdict.STRING[self.value]

class StopRequestEvent:
    def __init__(self, aComponent):
        self.component = aComponent

class StopRequestException(Exception):
    def __init__(self):
        Exception.__init__(self)
        
class ComponentDoneEvent:
    def __init__(self, aComponent):
        self.component = aComponent
        
class ComponentDoneExpectation:
    def __init__(self, aComponent):
        self.component = aComponent

    def match(self, aEvent):
        if isinstance(aEvent, ComponentDoneEvent):
            return aEvent.component == self.component
        elif aEvent == None:  
            # isAlive is threading.Thread method
            # only when thread is not running we now for sure it is done
            # the ComponentDoneEvent may be handled as well when the thread is about to die
            if not self.component.isAlive() :
                return True
        
class ComponentContext():
    def __init__(self, aMtc, aSystem, aParent):
        self.mtc = aMtc
        self.system = aSystem
        self.parent = aParent
        
class Component(threading.Thread):
    def __init__(self, aContext, aName, aStayAlive):
        threading.Thread.__init__(self, None, None, aName)
        self.context = aContext
        self.evQueue = EventQueue()
        self.name = aName
        self.stayAlive = aStayAlive
        self.defaults = []
        self.verdict = Verdict()
        
    def createContext(self):
        return ComponentContext(
            self.context.mtc,
            self.context.system,
            self 
        )
        
    def setVerdict(self, aVerdict):
        self.verdict.take(aVerdict)
        
    def getVerdict(self):
        return self.verdict.get()
    
    def stop(self):
        self.evQueue.put(StopRequestEvent(self))
        
    def handleSpecialEvent(self, aEvent):
        if      isinstance(aEvent, StopRequestEvent):
            # TODO still, this only happens on blocking actions :/
            raise StopRequestException()
            return True
        elif isinstance(aEvent, ComponentDoneEvent):
            self.verdict.take(aEvent.component.getVerdict().getValue())
            return True
    
    def handleAllSpecialEvents(self):
        # now this is messy :/
        q = []
        
        while not self.evQueue.empty():
            ev = self.evQueue.get()
            try :
                if not self.handleSpecialEvent(ev) :
                    new.append(ev)
            except StopRequestException:
                pass
        
        for ev in q :
            self.evQueue.put(ev)
            
    def executeBlockingAction(self, aAction):
        cmd = None
        repeat = True
        while repeat:
            # check without event (mostly for surplus .done)
            cmd = aAction.applies(None)
            
            # check with event and the explicit blocking statement
            if not cmd:
                ev  = self.evQueue.get()
                special = self.handleSpecialEvent(ev)
                cmd = aAction.applies(ev)
            
            # check the event with defaults
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
            elif not special :
                print("Unhandled event: " + str(ev))
    
    def log(self, aString):
        print(self.name + ": " + aString);
    
    def run(self):
        try:
            self.behaviour()
        except StopRequestException:
            self.log("Stop requested")
            pass
        except:
            self.log("Unexpected error")
            self.setVerdict(Verdict.ERROR)
            raise
            
        self.handleAllSpecialEvents()
        self.context.parent.evQueue.put(ComponentDoneEvent(self))
            
    def behaviour(self):
        pass

class Mtc(Component):
    def __init__(self):
        Component.__init__(self, None, "MTC", False)
        self.testcase = lambda : None
        
    def setContext(self, aContext):
        self.context = aContext
        
    def setTestcase(self, aTestcase):
        self.testcase = aTestcase
        
    def setParams(self, *aParams):
        self.params = aParams
        
    def run(self):
        self.testcase(self, *self.params)
        self.handleAllSpecialEvents()

class Testcase:
    def __init__(self, aFunction, aMtcType, aSystemType):
        self.mtcType = aMtcType
        self.systemType = aSystemType
        self.function = aFunction
        
class Control():
    def execute(self, aTestcase, *aParameters):
        mtc = aTestcase.mtcType()
        # system = aTestcase.systemType()
        system = None
        
        mtc.setContext(ComponentContext(mtc, system, None))
        
        mtc.setTestcase(aTestcase.function)
        mtc.setParams(*aParameters)
        
        mtc.start()
        mtc.join()
        
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
