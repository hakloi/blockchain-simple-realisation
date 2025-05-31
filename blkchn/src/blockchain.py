from transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain = [] 

    def add_transaction(self, transaction):
        self.chain.append(transaction)

    def find_transaction(self, tx_id):
        for tx in self.chain:
            if tx.id == tx_id:
                return tx
        return None

    def get_full_chain(self):
        return [tx.to_dict() for tx in self.chain]
