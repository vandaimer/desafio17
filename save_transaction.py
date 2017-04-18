# coding: utf-8
def save_transaction(row):
    user_id = row[0]
    order = row[1].strip()
    amount = float(row[2])
    if transactions.get(user_id):
        transaction = transactions[user_id]
        transaction['order'] = "%s, %s" % (transaction['order'], order) # tentar melhorar
        transaction['amount'] += amount
    else:
        transactions[user_id] = {'order': order, 'amount': amount}
        
