"""
Central ID generator.
"""


class IDGenerator:

    def __init__(self, start: int):
        self.current = start

    def next(self):

        value = self.current

        self.current += 1

        return value