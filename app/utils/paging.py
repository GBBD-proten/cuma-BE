class Paging:
    _instance = None
    
    @classmethod
    def get_instance(cls,page=None,size=None):
        if cls._instance is None:
            cls._instance = cls(page,size)
        return cls._instance
    
    def __init__(self, page, size):
        # if page is None:
        #     page = 1
        # if size is None:
        #     size = 10
        
        self._startNum = None
        self._endNum = None
        
        self.set_paging(page,size)
        
        
    def set_paging(self,page,size):
        self._startNum = str((page-1)*size)
        self._endNum = str(page*size)
        