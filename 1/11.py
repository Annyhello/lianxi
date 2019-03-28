class A:
    def add(self, x):
        y = x + 1
        print(y)


class B(A):
    def add(self, x):
        super().add(x)


b = B()
b.add(2)