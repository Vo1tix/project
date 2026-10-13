class HalfHistory:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.actions = []
        self.copies = 0

    def add(self, action):
        if len(self.actions) == self.capacity:
            half = (self.capacity + 1) // 2
            rest = self.actions[half:]
            self.copies += len(rest)
            self.actions = rest
        self.actions.append(action)

    def get_actions(self):
        return list(self.actions)

    def __len__(self):
        return len(self.actions)


class OneHistory:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.actions = []
        self.copies = 0

    def add(self, action):
        if len(self.actions) == self.capacity:
            rest = self.actions[1:]
            self.copies += len(rest)
            self.actions = rest
        self.actions.append(action)

    def get_actions(self):
        return list(self.actions)

    def __len__(self):
        return len(self.actions)