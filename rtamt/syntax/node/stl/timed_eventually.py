from rtamt.semantics.interval.interval import Interval
from rtamt.syntax.node.unary_node import UnaryNode

class TimedEventually(UnaryNode, Interval):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """
    def __init__(self, child, interval, is_pure_python=True):
        """Constructor for Eventually node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        UnaryNode.__init__(self, child)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'eventually[' + str(self.begin) + str(self.begin_unit) + ',' + str(self.end) + str(self.end_unit) + '](' + child.name + ')'
