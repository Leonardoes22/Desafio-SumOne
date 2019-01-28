from operator import attrgetter

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
