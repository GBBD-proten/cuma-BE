class Paging:
    def __init__(self, page: int = 1, size: int = 10):

        self.page = page
        self.size = size
        
        self.setPaging()
        
    def setPaging(self):
        self._startNum = (self.page - 1) * self.size
        self._endNum = self.page * self.size
    
    @property
    def startNum(self) -> int:
        return self._startNum
    
    @property
    def endNum(self) -> int:
        return self._endNum

    
        