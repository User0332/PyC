class a:
    def __add__(self, other):
        print("a->add")
        return NotImplemented

    def __radd__(self, other):
        print("a->radd")
        return NotImplemented

class b:
    def __add__(self, other):
        print("b->add")
        return NotImplemented

    def __radd__(self, other):
        print("b->radd")


x = a()
y = b()

print(x+y)