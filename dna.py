import sys
from enum import IntEnum
from typing import Iterator


class Nucleotide(IntEnum):
    A = 0
    C = 1
    G = 2
    T = 3


class Sequence:

    MASK_2 = (1 << 2) - 1
    MASK_6 = (1 << 6) - 1

    def __init__(self, idx: int, chunk: bytes) -> None:
        self.idx = idx
        self.nucleotides = ""
        self.quality = ""
        for byte in chunk:
            self.nucleotides += Nucleotide(byte & self.MASK_2).name
            self.quality += chr((byte & self.MASK_6) + 33)

    def __str__(self) -> str:
        line_1 = f"@READ_{self.idx}"
        line_3 = f"+READ_{self.idx}"
        return "\n".join([line_1, self.nucleotides, line_3, self.quality])

    def __repr__(self) -> str:
        return f"<Sequence: {self.nucleotides}; {self.quality}>"


def chunks_generator(input_file: str, length: int) -> Iterator[bytes]:
    try:
        with open(input_file, "rb") as f:
            for chunk in iter(lambda: f.read(length), b""):
                yield chunk
    except IOError:
        sys.exit(f"Unable to read '{input_file}'")


def main() -> None:
    try:
        _, input_file, length = sys.argv
    except ValueError:
        sys.exit("Please provide exactly two arguments")
    if int(length) <= 0:
        sys.exit("Length must be greater than 0")
    for idx, chunk in enumerate(chunks_generator(input_file, int(length)), 1):
        print(Sequence(idx, chunk))


if __name__ == "__main__":
    main()
