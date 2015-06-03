
from myorg.package1.check_services import check_services

def test_2():
    c =  check_services()
    okay = False
    for ci in c:
        if type(ci.values()[0]) == float:
            okay = True
    if not okay:
        raise ValueError('Did not find float results in all dictionaries of %r' % c)