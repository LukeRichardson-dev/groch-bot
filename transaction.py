class Transaction:
    def __init__(self, jsonData: dict) -> None:
        self.to = jsonData.get('to')
        self.from_ = jsonData.get('from')
        self.amount = jsonData.get('amount')
        self.on = jsonData.get('on')

    def toMap(self):
        return {
            'to': self.to,
            'from': self.from_,
            'amount': self.amount,
            'on': self.on
        }