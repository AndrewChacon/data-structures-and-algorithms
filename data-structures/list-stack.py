
class ListStack: # Last in First out 
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)
    
    def pop(self): # LIFO
        return self._L.pop()
    
    def peek(self): # LIFO
        return self._L[-1]
    
    def __len__(self):
        return len(self._L)
    
    def isEmpty(self):
        return len(self) == 0 # True or False
    