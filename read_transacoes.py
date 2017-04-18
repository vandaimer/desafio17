# coding: utf-8
with open('transacoes.csv','r') as f:
    reader = csv.reader(f)
    headers = next(reader)[1:]
    for row in reader:
        print(row)
get_ipython().magic('save read_transacoes 13')
