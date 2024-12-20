class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int) -> None:
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("Dequeue from an empty queue")

# Example Usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  
    q.enqueue(3)
    print(q.dequeue())  
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue()) 
    print(q.dequeue())  
    print(q.dequeue()) 

    try:
        print(q.dequeue())  
    except IndexError as e:
        print(e)  