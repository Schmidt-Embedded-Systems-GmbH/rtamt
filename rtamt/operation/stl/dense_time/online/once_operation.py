from rtamt.operation.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation


class OnceOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.prev = - float("inf")

    def update(self, node, sample, *args, **kargs):
        sample_result = []

        for i in sample:
            out_time = i[0]
            out_value = max(i[1], self.prev)

            sample_result.append([out_time, out_value])
            self.prev = out_value

        return sample_result

    def update_final(self, node, sample, *args, **kargs):
        return self.update(node, sample, *args, **kargs)
