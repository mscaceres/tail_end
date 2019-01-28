from enum import Enum

class Color(Enum):
    RED = 91
    BLUE = 94
    GREEN = 92
    MAGENTA = 95
    YELLOW = 93
    BLACK = 90
    CYAN = 96


class Tick:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char

    # Agregar validaciones a todos estos metodos
    def __mul__(self, value):
        return self.__class__(self.char * value)

    def __getitem__(self, index):
        return self.__class__(self.char[index])

    def __add__(self, other):
        return self.__class__(self.char + other)

    def __len__(self):
        return len(self.char)


class ColorTick(Tick):
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
        if other.CURRENT == self.CURRENT:
            # same color, maybe different char
            return super().__add__(other)
        else:
            return MixedColor(self, other)

    def __format__(self, format_spec):
        import pdb;pdb.set_trace()
        return format_spec.format(str(self))


class MixedColor():

    def __init__(self, *tick_colors):
        self.tick_colors = tick_colors



# create a subclass of ColorTrick per color defined
globals().update((tick_color.name+'Tick',
                  type(tick_color.name+'Tick', (ColorTick,), {'CURRENT':tick_color,
                                                              '_START': f'\33[{tick_color.value}m'}))
                 for tick_color in Color)
