from dna import Sequence


def test_bytes():
    seq = Sequence(1, b"R\xcd\x03\x91\x08\x18\xc5O\xc1\x15")
    assert str(seq) == '@READ_1\nGCTCAACTCC\n+READ_1\n3.$2)9&0"6'


def test_empty():
    seq = Sequence(0, b"")
    assert str(seq) == "@READ_0\n\n+READ_0\n"
