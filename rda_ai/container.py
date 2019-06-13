

class Container:

    def __init__(self, name):
        self.name = name
        self.values = []
        self.subnames = []

    def __str__(self):
        s = f"{self.name} ({self.get_totals():.4f})\n"
        for n in self.subnames:
            if type(self.values[self.subnames.index(n)]) == Container:
                s += " - " + str(self.values[self.subnames.index(n)]).replace("\n", "\n  ")
            else:
                s += f" - {n}: {self.values[self.subnames.index(n)]:.4f}\n"
        return s

    def add_item(self, name, value):
        if name in self.get_names():
                i = self._find_subname(name)
                if type(self.values[i]) == Container:
                    self.values[i].add_item(name, value)  # Sub-recursive.
                else:
                    self.values[i] += value
        else:
            self.subnames.append(name)
            self.values.append(value)
        #print(f"Container added {name}: {value}")

    def get_totals(self):
        """
        :return: Assumes value is arithmetic and returns total.
        """
        return sum(map(lambda x: x.get_totals() if type(x) == Container else x, self.values))

    def get_value(self, name):
        val = self.values[self._find_subname(name)]
        return val.get_value(name) if type(val) == Container else val

    def get_names(self):
        ret_list = []
        for s in self.subnames:
            if type(self.values[self.subnames.index(s)]) == Container:
                ret = self.values[self.subnames.index(s)].get_names()  # Sub-Recursive.
                ret_list += ret
            elif type(s) == str:
                ret_list.append(s)
            elif type(s) == tuple:
                ret_list += list(s)
            else:
                print(f"container get_name error type {s} {type(s)}")
        return ret_list

    def _find_subname(self, name):
        i = 0
        for s in self.subnames:
            if type(self.values[self.subnames.index(s)]) == Container:
                if self.values[self.subnames.index(s)]._find_subname(name) is not None:
                    return i
            if type(s) == str and s == name:
                return i
            elif type(s) == tuple:
                for st in s:
                    if name == st:
                        return i
            i += 1
        return None
