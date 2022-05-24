from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation

class OnceOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = max(sample, self.prev_out)
        self.prev_out = sample_return
        return sample_return