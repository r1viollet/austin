import sys
import typing as t
from ctypes import CDLL, POINTER, Structure, c_char_p, c_int, c_ulong, c_void_p
from test.cunit import SRC
from types import ModuleType

la = CDLL(str(SRC / "libaustin.so"))


class Frame(Structure):
    _fields_ = [
        ("key", c_ulong),
        ("filename", c_char_p),
        ("scope", c_char_p),
        ("line", c_int),
    ]


la.austin_pop_frame.restype = POINTER(Frame)

la.austin_read_frame.argtypes = [c_void_p, c_ulong]
la.austin_read_frame.restype = POINTER(Frame)


sys.modules[__name__] = t.cast(ModuleType, la)
