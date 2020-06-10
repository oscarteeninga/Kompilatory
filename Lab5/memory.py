class Memory:
    def __init__(self, parent=None):
        self.parent = parent
        self.values = {}

    def put(self, name, value):
        self.values[name] = value

    def get(self, name):
        if str(name) in self.values:
            return self.values[str(name)]
        if self.parent is not None:
            return self.parent.get(name)
        return None

    def has_key(self, name):
        if name in self.values:
            return True
        if self.parent is not None:
            return self.parent.has_key(name)
        return False


class LoopScope(Memory):
    pass


class FunctionScope(Memory):
    pass


class IfScope(Memory):
    pass
