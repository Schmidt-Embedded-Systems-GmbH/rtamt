import collections
from rtamt.operation.abstract_online_operation import AbstractOnlineOperation
class HistoricallyTimedOperation(AbstractOnlineOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            val = float("inf")
            self.buffer.append(val)

    def update(self, node, sample):
        self.buffer.append(sample)
        sample_return = float("inf")
        for i in range(self.end-self.begin+1):
            sample_return = min(sample_return, self.buffer[i])
        return sample_return
