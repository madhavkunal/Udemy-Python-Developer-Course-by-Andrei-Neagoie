# debugging - act of finding and removing bugs, errors, and exceptions
# linting - allows us to detect code issues while coding live
# IDE (Integrated Development Environment) - Ex) VS Code, PyCharm, Sublime Text, etc.
# read errors - read tracebacks and understand error types - Ex) SyntaxError, NameError, TypeError, ValueError, AttributeError
# pdb - python debugger - built-in-module in python
# pdb.set_trace() - useful pdb method that gives us a live interactive python debugger

import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, "gdrfgd")
