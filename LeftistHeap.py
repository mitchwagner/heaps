"""
We recursively define a heap to be a 3-tuple (l,e,r), where e is a 
singleton set, and each of l and r is either a heap or the empty set. 
We refer to e as the root element of a heap, and l and r as subtrees 
of a heap.

We define the rank of a heap as follows. For a given heap, recursively 
select the heap's right subtree, until the subtree we select is the 
empty set. The rank of a heap is given by the number of selections
performed before selecting the empty set.

In a leftist heap, the rank of the heap's left subtree is greater than 
or equal to the rank of the heap's right subtree. Furthermore, each 
subtree of a leftist heap must be a leftist heap, or the empty set.

In the following implementation, we use the following symbols: 
    - e: the root element of a heap
    - s: the rank of a heap subtree 
    - n: the number of elements in a heap
    - l: the left subtree of a heap
    - r: the right subtree of a heap

This implementation is derived from the recursive definition of a 
heap; that is, the heap class is self-referencing.

"""

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class EmptyHeapException(Exception):
    pass    


class LeftistHeap(Generic[T]):
    
    e: Optional[T] = None
    s: int = 0
    l: 'Optional[LeftistHeap[T]]' = None
    r: 'Optional[LeftistHeap[T]]' = None
    n: int = 0 

    def __init__(self, e=None) -> None:
        self.e = e 
        if e:
            self.n = 1


    def min(self) -> T:
        '''
        O(1)
        '''
        if not self.e: 
            raise EmptyHeapException() 

        return self.e 


    def insert(self, e) -> None:
        '''
        O(log(n))
        '''
        new_heap: 'LeftistHeap[T]' = LeftistHeap(e)

        self.merge(new_heap)


    def delete_min(self) -> None:
        '''
        O(log(n))
        '''
        if self.empty():
            raise EmptyHeapException()

        if not self.l: 
            self.e = None 
            self.n = 0

        else:
            left = self.l
            right = self.r

            self.n = left.n
            self.e = left.e

            self.l = left.l
            self.r = left.r

            self.merge(right)


    def empty(self) -> bool:
        '''
        O(1)
        '''
        return self.n == 0


    def size(self) -> int:
        '''
        O(1)
        '''
        return self.n

  
    def merge(self, other: 'Optional[LeftistHeap[T]]') -> None:
        '''
        O(log(n))
        '''
        if not other:
            return

        self.n += other.n

        if not self.e:
            self.e = other.e
            return

        if self.min() > other.min():
            self.swap_root(other)
        
        if not self.r: 
            self.r = other
        else:
            self.r.merge(other)

        if self.r and not self.l:
            self.swap_children()

        elif self.r and self.l and self.r.s > self.l.s:
            self.swap_children()

        if not self.r:
            self.s = 0

        else:
            self.s = self.r.s + 1


    def swap_root(self, other) -> None:
        temp = self.e
        self.e = other.e
        other.e = temp 


    def swap_children(self) -> None:
        temp = self.l
        self.l = self.r
        self.r = temp


    def preorder(self):
        '''
        O(n)
        '''
        yield self.e

        if self.l:
            yield from self.l.preorder()

        if self.r:
            yield from self.r.preorder()


    def inorder(self):
        '''
        O(n)
        '''
        if self.l:
            yield from self.l.inorder()

        yield self.e

        if self.r:
            yield from self.r.inorder()


    def postorder(self):
        '''
        O(n)
        '''
        if self.l:
            yield from self.l.postorder()

        if self.r:
            yield from self.r.postorder()

        yield self.e


    def pretty_print(self) -> None:
        if not self.e:
            print("Empty")
            return

        self.pretty_print_recursive(0)


    def pretty_print_recursive(self, i) -> None:
        spacer = " " * 2 * i
        print(spacer + str(self.e) \
            + ", s=" + str(self.s) \
            + ", n=" + str(self.n))
        
        print(spacer + "left:")
        if self.l:
            self.l.pretty_print_recursive(i + 1)
        
        print(spacer + "right:")
        if self.r:
            self.r.pretty_print_recursive(i + 1)

