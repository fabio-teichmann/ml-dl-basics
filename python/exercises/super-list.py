class SuperList(list):
    def __len__(self):
        return 1000


sl = SuperList()

print(len(sl))
print(sl.append(4))
print(sl[0])
