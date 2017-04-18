# coding: utf-8
with open('usuarios.csv','r') as f:
    reader = csv.reader(f)
    headers = next(reader)[1:]
    for row in reader:
        print(row)
        
