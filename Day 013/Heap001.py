class MaxHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def _getLeftChildindex(self,index):
        return (index * 2) + 1
    

    @staticmethod
    def _getRightChildindex(self,index):
        return (index * 2)+ 2
    
    @staticmethod
    def _getParentIndex(self,index):
        return (index - 1) // 2