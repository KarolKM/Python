class Queue():
    def __init__(self, fifo):
        self.fifo = fifo

    def show(self):
        print(self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, element):
        self.fifo.append(element)

    def get(self):
        element = self.fifo.pop(0)
        return element



example_queue = Queue([21,1,2,2,3,4,423,13,42])
example_queue.show()
print(example_queue.is_empty())
example_queue.put(19)
example_queue.put(21)
example_queue.show()
example_queue.get()
example_queue.show()
