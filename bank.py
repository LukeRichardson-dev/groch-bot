from transaction import Transaction
from client_user import Client
import json
import time

class BankSerializer:
    def __init__(self, jsonData):
        self.clients: list = list(map(lambda x: Client(x), jsonData['clients']))

    def dump(self, fp):
        with open(fp, 'w') as f:
            json.dump({
                'clients': list(map(lambda x: x.toMap(), self.clients))
            }, f, indent=2)

class Bank:
    def __init__(self, fp: str):
        self.fp = fp
        self.bankStore = BankSerializer(self.data())

    def data(self):
        with open(self.fp) as f:
            return json.load(f)

    def getClient(self, client: Client):
        chosenClient = None
        i: Client
        for i in self.bankStore.clients:
            if i.id == client.id:
                chosenClient = i

        if chosenClient == None:
            self.bankStore.clients.append(client)
            chosenClient = client

        return chosenClient

    def add(self, client: Client, amount: int):
        chosenClient = self.getClient(client)

        chosenClient.balance += amount
        self.bankStore.dump(self.fp)

    def give(self, _from: Client, to: Client, amount: int):
        toStore = self.getClient(to)
        fromStore = self.getClient(_from)

        toStore.payment_history.append(
            Transaction(
                {
                    'to': toStore.id,
                    'from': fromStore.id,
                    'amount': amount,
                    'on': time.time(),
                }
            )
        )
        toStore.balance += amount
        fromStore.balance -= amount

        self.bankStore.dump(self.fp)

    def getMoney(self, client: Client):
        user = self.getClient(client)

        return user.balance