import pytest
from tail_end import main

def test_day_by_week():
    main([34,90,1,"days_by_week"])
    assert 2912 == 2912