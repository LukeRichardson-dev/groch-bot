import json


class NewCounter:
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
        return data['counters'].get(name)

    def add(self, name, value):
        data = self.load()

        counter = data['counters'][name]
        data['counters'][name] = counter + value

        self.write(data)

        return data['counters'][name]

    @property
    def counters(self):
        data = self.load()

        return data['counting']

    def add_counter(self, counter):
        data = self.load()

        data['counting'].append(counter)
        data['counters'][counter] = 0

        self.write(data)