from rtamt.operation.abstract_online_operation import AbstractOnlineOperation


class AbsOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, node, sample):
        sample_result = abs(sample)
        return sample_result