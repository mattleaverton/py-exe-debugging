"""

"""
from data import data_manager


class Bakery(object):
    def __init__(self, name: str):
        self.name = name.capitalize()

    def serve(self, confection: str, test_mode: bool = False):
        baked_good = data_manager.get_baked_good(confection.capitalize(), test_mode=test_mode)
        print(f"Welcome to {self.name} Bakery - please enjoy your '{baked_good}'")


if __name__ == "__main__":
    bk = Bakery("Buntastic")
    bk.serve("croissant", test_mode=True)
