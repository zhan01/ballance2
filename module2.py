from module1 import balance, transactions

def apply_transactions(balance, transactions):
    for transaction in transactions:
        for key,val in transaction.items():
            user = key
            value = val
            balance[user] += value
    return balance

 
newBalance = apply_transactions(balance, transactions)
print(newBalance)