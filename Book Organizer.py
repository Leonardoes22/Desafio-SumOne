from operator import attrgetter
import csv

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

def organize(rule, collection):
    if(rule == []):
        return []
    elif(rule[0][0] == "Null"):
        raise Exception('OrderingException')
    for r in rule:
        if(r[1] == 'desc'):
            desc = True
        else:
            desc = False
        collection = sorted(collection, key=attrgetter(r[0]), reverse=desc)
    return collection

def load_data(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        return list(reader)
#---------------------------------------------------------------------------

config_rule = load_data('config.csv')
collection = load_data('collection.csv')

book_collection = []
for b in collection:
    book_collection.append(Book(b[0],b[1],b[2]))
