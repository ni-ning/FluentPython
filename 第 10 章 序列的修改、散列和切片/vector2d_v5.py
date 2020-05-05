# coding: utf-8

from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
    type_code = 'd'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # 长度有限的表示形式 如 '[111, 111, 111, 111, 111, 111, ...]'
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self._components))

    def __bytes__(self):
        return (bytes([ord(self.type_code)])) + bytes(self._components)

    def __eq__(self, other):
        return (len(self) == len(other)) \
               and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{.__name__} indices must be integer'
            raise TypeError(msg.format(cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))
