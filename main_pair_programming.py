class Integer(int):

    def __init__(self, integer):
        self.integer = integer

    def __max__(self, other) -> int:
        return max(self.integer, other.integer)
    
    def __min__(self, other) -> int:
        return min(self.integer, other.integer)

    def isPositive(self) -> bool:
        return True if self.integer >= 0 else False
