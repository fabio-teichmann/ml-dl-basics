# MRO = determines the order in which to inherit
class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)

for i, l in enumerate(D.mro()):
    print(i, l)
