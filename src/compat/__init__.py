"""
python 2.4 - python 3.2 compatibility shim
"""

import inspect


class TimeoutError(OSError):
    """shims in the TimeoutError used in python 3.3 and up"""


inspect.ArgSpec.parameters = inspect.ArgSpec.args
inspect.signature = inspect.getargspec
