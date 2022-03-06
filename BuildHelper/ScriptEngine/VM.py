"""
Virtual Machine
"""
from . import BaseMachine


class Preprocessor:
    def __init__(self, code):
        self.stack = []
        self.out = []
        wait = []
        end = []
        for i in code:
            if len(wait) != 0:
                self.out += self.stack
                self.out.append(i)
                self.out += wait
                wait.pop()
                self.stack = []
            elif (i in BaseMachine.keyword_set) and (i in BaseMachine.start_end_set):
                end.append(i)
            elif (i in BaseMachine.keyword_set) and (i in BaseMachine.wait_set):
                wait.append(i)
            elif (i in BaseMachine.keyword_set) and (i not in BaseMachine.wait_set):
                self.out.append(i)
            else:
                self.stack.append(i)
        self.out += self.stack + end
        
        
class Engine(BaseMachine):
    def __init__(self):
        super(Engine, self).__init__()
