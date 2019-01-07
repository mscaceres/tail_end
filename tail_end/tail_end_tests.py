import pytest
from tail_end import tail_end

@pytest.mark.parametrize("args, results", [
    [(10, 20, 1), (10, 20, 10)],
    [(10, 20, 2), (20, 40, 20)],
    [(10, 30, 1), (20, 30, 10)],
    [(37, 70, 15), (495, 1050, 555)],
])
def test_days_by_year(args, results):
    kw = dict(zip(('time_doing', 'time_total', 'times'), args))
    r, t, w, u = tail_end(unit='days_by_years', **kw)
    assert u == 'days'
    assert (r, t, w) == results


@pytest.mark.parametrize("args, results", [
    [(10, 20, 1), (520, 1040, 520)],
    [(10, 20, 7), (3640, 7280, 3640)]
])
def test_days_by_week(args, results):
    kw = dict(zip(('time_doing', 'time_total', 'times'), args))
    r, t, w, u = tail_end(unit='days_by_weeks', **kw)
    assert u == 'days'
    assert (r, t, w) == results


@pytest.mark.parametrize("args, results", [
    [(10, 20, 1), (120, 240, 120)],
    [(10, 20, 7), (840, 1680, 840)]
])
def test_days_by_month(args, results):
    kw = dict(zip(('time_doing', 'time_total', 'times'), args))
    r, t, w, u = tail_end(unit='days_by_months', **kw)
    assert u == 'days'
    assert (r, t, w) == results
