import json
from transaction import Transaction

class Client:
    def __init__(self, jsonData: dict):
        self.id = jsonData.get('id')
        self.nickname = jsonData.get('nickname')
        self.balance = jsonData.get('balance') if jsonData.get('balance') != None else 10.0
        self.payment_history = list(map(lambda x: Transaction(x), jsonData.get('payment_history') if jsonData.get('payment_history') != None else []))
        self.intrest_rate = jsonData.get('intrest_rate') if jsonData.get('intrest_rate') != None else 10.0

    def toMap(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'balance': self.balance,
            'payment_history': list(map(lambda x: x.toMap(), self.payment_history)),
            'intrest_rate': self.intrest_rate,
        }

    def toJson(self):
        return json.dumps(self.toMap())