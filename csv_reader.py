import csv
import os
import re
from app import app


class CSVReader(object):
    def __init__(self, file_path=None):
        if file_path is None:
            raise ValueError('The file path is require.')
        self.file_path = os.path.join(app.root_path, file_path)
        self.data = {}
        self.read_data()

    def read_data(self):
        try:
            with open(self.file_path,'r') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    self.add_item(row)
        except (FileNotFoundError, IOError):
            print("File not found.")

    def get_data(self):
        return self.data

    def add_item(self, item):
        raise NotImplementedError('This method needs be overwritten.')


class UserCSVReader(CSVReader):
    def add_item(self, item):
        self.data[item[0]] = {'name': item[1].strip(), 'phone': item[2].strip()}


class TrasactionCSVReader(CSVReader):
    REGEX_SPLIT_ORDER = re.compile('(\d+) (\w+)')

    def __init__(self, file_path=None):
        super().__init__(file_path)
        self._formater_orders()

    def add_item(self, item):
        id = item[0]
        order = item[1].strip()
        amount = float(item[2])
        if self.data.get(id):
            transaction = self.data[id]
            transaction['order'] = "%s,%s" % (transaction['order'], order) # tentar melhorar
            transaction['amount'] += amount
        else:
            self.data[id] = {'order': order, 'amount': amount}

    def _formater_orders(self):
        for transaction in self.data.values():
            order = self.REGEX_SPLIT_ORDER.findall(transaction['order'])
            products = {}
            amount = 0
            for item in order:
                product_name = item[1]
                if products.get(product_name) is None:
                    products[product_name] = 1
                else:
                    products[product_name] += 1
            transaction['order'] = ', '.join(['%s %s' % (value, key) for key, value in products.items()])
