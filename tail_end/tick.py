from enum import Enum

class Color(Enum):
    RED = 91
    BLUE = 94
    GREEN = 92
    MAGENTA = 95
    YELLOW = 93
    BLACK = 90
    CYAN = 96


class ColorTick(str):
    AVAILABLE_COLORS = {}
    CURRENT = None
    _START = None
    _END = '\033[0m'

    @classmethod
    def __init_subclass__(cls):
        """update available colors when subclases are added"""
        cls.AVAILABLE_COLORS[cls.__name__] = cls

    @classmethod
    def from_color_string(cls, color, char):
        """Instanciate a ColorTick object"""
        cls_name = color.upper() + "Tick"
        return cls.AVAILABLE_COLORS[cls_name](char)

    def __str__(self):
        return self._START + super().__str__() + self._END

    def __add__(self, other):
        if isinstance(other, self.__class__.__bases__):
            if self == other:
                return self.__class__(super().__add__(other))
            else:
                return MixedColor(self, other)
        elif isinstance(other, str):
            return super().__add__(other)
        else:
            raise TypeError('Invalid type for %s' % other)

    def __format__(self, format_spec):
        return format(str(self), format_spec)

    def __mul__(self, value):
        return self.__class__(super().__mul__(value))

    def __getitem__(self, index):
        return self.__class__(super().__getitem__(index))

    def __eq__(self, other):
        return self.CURRENT == other.CURRENT and super().__eq__(other)


class MixedColor():

    def __init__(self, *tick_colors):
        self.tick_colors = tick_colors

    def __str__(self):
        return "".join(str(tick_color) for tick_color in self.tick_colors)

    def __format__(self, format_spec):
        return format(str(self), format_spec)


# create a subclass of ColorTrick per color defined
globals().update((tick_color.name+'Tick',
                  type(tick_color.name+'Tick',
                       (ColorTick,), {'CURRENT':tick_color, '_START': f'\33[{tick_color.value}m'}))
                 for tick_color in Color)
