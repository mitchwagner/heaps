from LeftistHeap import LeftistHeap as Heap

h = Heap()

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
