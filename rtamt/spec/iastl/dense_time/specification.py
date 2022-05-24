from rtamt.pastifier.stl.pastifier import StlPastifier
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, \
    AbstractOfflineOnlineSpecification

from rtamt.syntax.ast.parser.stl.specification_parser import StlAst
from rtamt.semantics.enumerations.options import *


def IASTLDenseTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlDenseTimeOfflineInterpreter(), IAStlDenseTimeOnlineInterpreter(semantics), pastifier=StlPastifier())
    else:
        raise Exception()

    return spec

def IAStlDenseTimeOfflineSpecification(semantics=Semantics.STANDARD):
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineInterpreter(semantics))
    return spec

def IAStlDenseTimeOnlineSpecification(semantics=Semantics.STANDARD):
    spec = AbstractOnlineSpecification(StlAst(), IAStlDenseTimeOnlineInterpreter(semantics), pastifier=StlPastifier())
    return spec
