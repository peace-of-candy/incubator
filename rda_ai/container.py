

class Container:

    def __init__(self, name):
        self.name = name
        self.values = []
        self.subnames = []

    def __str__(self):
        s = f"{self.name} ({self.get_totals():.4f})\n"
        for n in self.subnames:
            s += f" - {n}: {self.values[self.subnames.index(n)]:.4f}\n"
        return s

    def add_item(self, name, value):
        if name in self.get_names():
                i = self._find_subname(name)
                # print(f"Adding to already existing {name} {self.values[i]} with {self.values[i]+value}")
                self.values[i] += value
        else:
            self.subnames.append(name)
            self.values.append(value)
        #print(f"Container added {name}: {value}")

    def get_totals(self):
        """
        :return: Assumes value is arithmetic and returns total.
        """
        return sum(map(lambda x: x, self.values))

    def get_value(self, name):
        return self.values[self._find_subname(name)]

    def get_names(self):
        l = []
        for s in self.subnames:
            if type(s) == str:
                l.append(s)
            elif type(s) == tuple:
                l += list(s)
            else:
                print(f"container get_name error type {s} {type(s)}")
        return l

    def _find_subname(self, name):
        i = 0
        for s in self.subnames:
            if type(s) == str and s == name:
                return i
            elif type(s) == tuple:
                for st in s:
                    if name == st:
                        return i
            i += 1
        return None
