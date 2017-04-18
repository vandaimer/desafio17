# coding: utf-8
transactions = {}
with open('transacoes.csv','r') as f:
    reader = csv.reader(f)
    headers = next(reader)[1:]
    for row in reader:
        save_transaction(row)
regex_get_product = re.compile('(\d+) (\w+)')
#outra def
for transaction in transactions.values():
    order = regex_get_product.findall(transaction['order'])
    products = {}
    amount = 0
    for item in order:
        product_name = item[1]
        if products.get(product_name) is None:
            products[product_name] = 1
        else:
            products[product_name] += 1
    transaction['order'] = ', '.join(['%s %s' % (value, key) for key, value in products.items()])
    
