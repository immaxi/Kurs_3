#Задача 3. Яровенко Максим, ИУ5Ц-72Б

from random import randint

def gen_random(kolvo, min, max):                           
    for k in range(kolvo):
        i = randint(min, max)
        yield i

class Unique(object):

    def __init__(self, items, **kwargs):
        self.items = items
        if len(kwargs) != 0:
            if len(kwargs) != 0:
                self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False
        self.count = 0
        self.prsp = []

    def __next__(self):
        if type(self.items) != list:
            sp = []
            for i in self.items:
                sp.append(i)
            self.items = sp
             
        while True:
            if self.count < len(self.items):
                element = self.items[self.count]
                self.count += 1
                if self.ignore_case:
                    if element.lower() not in self.prsp:
                        self.prsp.append(element.lower())
                        return element
                else:
                    if element not in self.prsp:
                        self.prsp.append(element)
                        return element
            else:
                raise StopIteration
        
           

    def __iter__(self):
        return self
                

data = ['ABc', 'ab', 'bca', 'ab', 'abc', 'Ab', 'c']

for i in Unique(data, ignore_case=True):
    print(i)

data = gen_random(15, 1, 5)

for i in Unique(data):
    print(i)

input("Press Enter to continue...")



