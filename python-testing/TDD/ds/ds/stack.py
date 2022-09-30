class Stack:
    """
    This was developed using TDD
    Running tests: python -m pytest -v
    Running tests with coverage: python -m pytest -v --cov
    """

    def __init__(self):
        self._storage = list()


    def __len__(self):
        return len(self._storage)


    def push(self, item):
        self._storage.append(item)


    def pop(self):
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item