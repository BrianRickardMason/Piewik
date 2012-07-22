
from Event import * 
        
class Example(Testcase):
    def __init__(self):
        def execute(self, aPass, aFail, aInconc):
            if aPass :
                self.setVerdict(Verdict.PASS)
            if aFail :
                self.setVerdict(Verdict.FAIL)
            if aInconc :
                self.setVerdict(Verdict.INCONC)
            
        Testcase.__init__(self, execute, Mtc, None);

ctrl = Control()
for a in [True, False]:
    for b in [True, False]:
        for c in [True, False]:
            ctrl.execute(Example(), a, b, c)
