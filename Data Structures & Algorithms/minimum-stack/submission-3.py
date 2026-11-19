class MinStack:

    def __init__(self):
        self.value=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.value.append(val)
        val=min(val,self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        self.value.pop()
        self.min.pop()

    def top(self) -> int:
        return self.value[-1]

    def getMin(self) -> int:
        return self.min[-1]
