from module1 import balance, transactions

def apply_transactions(balance, transactions):
    for transaction in transactions:
        for user,value in transaction.items():
            balance[user] += value
    return balance

 
print(apply_transactions(balance, transactions))
