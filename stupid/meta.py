from abc import ABCMeta
from dataclasses import dataclass

class StupidMeta(ABCMeta):
    def __new__(mcls, name, bases, namespace, **kwargs):
        inherited_annotations = {}
        for base in bases:
            try:
                inherited_annotations.update(base.__annotations__)
            except AttributeError:
                pass

        try:
            annotations = dict(**namespace['__annotations__'], **inherited_annotations)
        except KeyError:
            annotations = inherited_annotations

        if annotations:
            namespace['__annotations__'] = annotations
        namespace['__slots__'] = ()

        bases = tuple(base.__stupid__ if hasattr(base, '__stupid__') else base for base in bases)
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)

        slots = tuple(annotations.keys())
        {slot: namespace.pop(slot, None) for slot in slots}
        namespace['__slots__'] = slots
        namespace['__stupid__'] = cls
        ncls = super().__new__(mcls, name, bases, namespace, **kwargs)

        return ncls

    def __getattribute__(self, name):
        slots = super().__getattribute__('__slots__')
        if name in slots:
            stupid = super().__getattribute__('__stupid__')
            return getattr(stupid, name)
        return super().__getattribute__(name)

    def __instancecheck__(cls, instance):
        return super(StupidMeta, cls.__stupid__).__instancecheck__(instance)

class Stupid(metaclass=StupidMeta):
    __slots__ = ()


class StupidDataMeta(StupidMeta):
    def __new__(mcls, name, bases, namespace, **kwargs):
        ncls = dataclass(super().__new__(mcls, name, bases, namespace, **kwargs))
        return ncls


class StupidData(metaclass=StupidDataMeta):
    __slots__ = ()
