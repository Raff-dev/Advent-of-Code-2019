
import pathlib

path = pathlib.Path(__file__).parent.resolve()

def load_input(day) -> list[str]:
    with open(path / f"input/day{day}.txt") as f:
        return f.read().splitlines()
