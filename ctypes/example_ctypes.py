# Step 1: Go to directory 'clib/build/', create it if it does not exsits.
# Step 2: Run cmd 'cmake .. && make'
# Step 3: Return to current directory and run this script.


import ctypes
import os

# Load the clib, checkout the c++ source file: clib.cc
_file = './clib/build/libclib.so'
_mod = ctypes.cdll.LoadLibrary(_file)

# Example 1
# Call a simple C function: double add(doube, double)
# Just use built-in ctypes.
_mod.add.argtypes = (ctypes.c_double, ctypes.c_double)
_mod.add.restype = ctypes.c_double
print(_mod.add(1, 2))

# Example 2
# Call a little complex C function: double average(double*, int N)
# Since python has many types which can represent an "array", for example, list
# tuple, ndarray, so we should specifiy the convertion by ourselves.
class DoubleArrayType:
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)

    # Cast from array.array objects
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))

    # Cast from lists/tuples
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val

    from_tuple = from_list

    # Cast from a numpy array
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

_mod.average.argtypes = (DoubleArrayType(), ctypes.c_int)
_mod.average.restype = ctypes.c_double

x = [1,2,3,4,5]
print(_mod.average(x, len(x)))

# Example 3
# Call functions with C struct as input. Note that the pointer of the input
# stcuture are used but not the structures themselves.
# struct Point { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double

print(_mod.distance(Point(0,0), Point(1,1)))