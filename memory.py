class Memory:
    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def __str__(self):
        return "\n".join(self.steps[-5:])
