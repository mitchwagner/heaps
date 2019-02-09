from LeftistHeap import LeftistHeap as Heap
import random

h = Heap()

'''
h.insert(9)
h.pretty_print()
print("-" * 79)

h.insert(3)
h.pretty_print()
print("-" * 79)

h.insert(2)
h.pretty_print()
print("-" * 79)

h.insert(6)
h.pretty_print()
print("-" * 79)

h.delete_min()
h.pretty_print()
'''

for i in range(10000):
    print(i)
    r = random.randint(0, 100)
    h.insert(r)


ls = []
while not h.empty():
    ls.append(h.min())
    h.delete_min()


def is_incrementing(ls):
    is_incr = True

    for i, val in enumerate(ls[1:]):
        if val < ls[i]:
            print("val", val)
            print("other")
            is_incr = False

    print(is_incr)

print(ls)
is_incrementing(ls)
