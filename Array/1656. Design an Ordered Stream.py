# There is a stream of n (id, value) pairs arriving in an arbitrary order, where id is an integer between 1 and n and value is a string. No two pairs have the same id.

# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

# Implement the OrderedStream class:

# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int id, String value) Inserts the pair (id, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * n
        self.s = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.list[id-1] = value
        temp = []
        for i in range(self.s,self.list):
            if self.list[i] == None:
                self.s = i
                break
            else:
                temp.append(self.list[i])
        return temp


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)