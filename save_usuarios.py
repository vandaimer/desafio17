# coding: utf-8
def save_user(row):
    users[row[0]] = {'name': row[1].strip(), 'phone': row[2].strip()}
    
