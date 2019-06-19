from .tick import *

def test_all_clases_created():
    l = globals()
    assert all( clr.name + 'Tick' in l for clr in Color) is True

def test_colotick_slice():
    blue_tick = ColorTick.from_color_string("blue", "#")
    blue_tick = blue_tick * 10
    slice_tick = blue_tick[5:7]
    assert type(slice_tick) == type(blue_tick)
    assert len(slice_tick) == 2


def test_colotick_mul():
    blue_tick = ColorTick.from_color_string("blue", "#")
    mul_tick = blue_tick * 10
    assert type(mul_tick) == type(blue_tick)
    assert len(mul_tick) == 10
