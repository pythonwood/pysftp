'''test pysftp.Connection compression param - uses py.test'''
from __future__ import print_function


def test_security_options(rsftp):
    '''test the security_options property has expected attributes and that
    they are tuples'''
    secopts = rsftp.security_options
    for attr in ['ciphers', 'compression', 'digests', 'kex']:
        print(attr)
        assert hasattr(secopts, attr)
        assert isinstance(getattr(secopts, attr), tuple)
    for attr in ['key_types', ]:
        print(attr)
        assert hasattr(secopts, attr)
        assert isinstance(getattr(secopts, attr), list)
