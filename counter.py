import json

class Counter:
    def __init__(self, fp):
        self.fp = fp

    def load(self):
        with open(self.fp) as f:
            return json.load(f)

    def write(self, data):
        with open(self.fp, 'w') as f:
            return json.dump(data, f)
    
    def get(self, name):
        data = self.load()
        return data.get(name)

    def add(self, name, value):
        data = self.load()

        counter = data[name]
        data[name] = counter + value

        self.write(data)

        return data[name]