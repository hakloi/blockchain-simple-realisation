import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from blockchain import Blockchain
from transaction import Transaction

def main():
    chain = Blockchain()

    # Создаём транзакцию с пустыми входами (например, награда)
    tx1 = Transaction(inputs=[], outputs=[{'address': 'Alice', 'amount': 50}])
    chain.add_transaction(tx1)

    # Alice отправляет 30 Bob'у
    tx2 = Transaction(inputs=[tx1.id], outputs=[{'address': 'Bob', 'amount': 30}, {'address': 'Alice', 'amount': 20}])
    chain.add_transaction(tx2)

    # Bob отправляет 10 Charlie
    tx3 = Transaction(inputs=[tx2.id], outputs=[{'address': 'Charlie', 'amount': 10}, {'address': 'Bob', 'amount': 20}])
    chain.add_transaction(tx3)

    for tx in chain.chain:
        print(tx)


if __name__ == '__main__':
    main()
