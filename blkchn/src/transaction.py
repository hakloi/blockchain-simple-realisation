import json
import hashlib
import uuid


class Transaction:
    def __init__(self, inputs, outputs):
        """
        inputs: список хэшей (id) предыдущих транзакций
        outputs: список словарей: {'address': str, 'amount': float}
        """
        self.id = str(uuid.uuid4()) 
        self.inputs = inputs
        self.outputs = outputs

    def to_dict(self):
        return {
            'id': self.id,
            'inputs': self.inputs,
            'outputs': self.outputs
        }

    def compute_hash(self):
        data = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(data).hexdigest()

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2)
