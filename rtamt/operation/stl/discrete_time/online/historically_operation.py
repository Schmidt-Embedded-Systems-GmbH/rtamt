from rtamt.operation.abstract_discrete_time_online_operation import AbstractDiscreteTimeOnlineOperation

class HistoricallyOperation(AbstractDiscreteTimeOnlineOperation):
    def __init__(self):
        self.prev_out = float("inf")

    def reset(self):
        self.__init__()

    def update(self, node, sample):
        sample_return = min(sample, self.prev_out)
        self.prev_out = sample_return
        return sample_return
