class calculate:
        def __init__(self, fileName, a, b):
                self.fileName = fileName
                self.a = a
                self.b = b
        def extract(self):
                file = open(self.fileName,'r')
                full_data = []
                for f in file:
                        row = f.split()
                        full_data.append(row)
                for row in full_data:
                        p = row[self.a]
                        q = row[self.b]
                return p,q
        def sum(self):
                r,s = calculate.extract(self)
                c = float(r) + float(s)
                return c
        def sub(self):
                r,s = calculate.extract(self)
                c = float(r) - float(s)
                return c
