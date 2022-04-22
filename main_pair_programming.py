class Integer(int):

    def __init__(self, integer):
        self.integer = integer

    def __max__(self, other) -> int:
        return max(self.integer, other.integer)
