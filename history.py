class Command_History:
    def __init__(self, max_size=100):
        self.history = []
        self.max_size = max_size

    def add(self, command):
        if command.strip():
            self.history.append(command)
            if len(self.history) > self.max_size:
                self.history.pop(0)

    def show(self):
        for i, cmd in enumerate(self.history, 1):
            print(f"{i}: {cmd}")
            
    def clear(self):
        self.history = []