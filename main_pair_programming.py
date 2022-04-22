class Integer(int):

    def __init__(self, integer):
        self.integer = integer

    def __max__(self, other) -> int:
        return max(self.integer, other.integer)
    
    def __min__(self, other) -> int:
        if self.integer < other.integer:
            return self.integer
        elif self.integer == other.integer:
            return self.integer
        else:
            return other.integer
