"""
A leftist heap is a priority queue with the property that, for each node in
the queue, the node's left child must be of equal or further distance to the
nearest leaf than the child's right node.

We thus define the rank of a node to be the number of edges separating 
a node and its rightmost descendant.

In the following implementation, we use the following symbols: 
    - e: the element stored by a node
    - s: the rank of a node
    - l: the left subtree of a heap
    - r: the right subtree of a heap
    - n: the number of elements in the heap

This implementation is derived from the recursive definition of a 
heap; that is, the heap class is self-referencing.

"""

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class EmptyHeapException(Exception):
    pass    


class Node(Generic[T]):

    def __init__(self, e=None):
        self.e: T = e
        self.s: int = 0


class LeftistHeap(Generic[T]):
    
    root: Optional[Node[T]] = None
    l: 'Optional[LeftistHeap[T]]' = None
    r: 'Optional[LeftistHeap[T]]' = None
    n: int = 0 

    def __init__(self, root=None) -> None:
        self.root = root
        if root:
            self.n = 1


    def min(self) -> T:
        '''
        O(1)
        '''
        if not self.root: 
            raise EmptyHeapException() 

        return self.root.e 


    def insert(self, e) -> None:
        '''
        O(log(n))
        '''
        node: Node[T] = Node(e)
        new_heap: 'LeftistHeap[T]' = LeftistHeap(root=node)

        self.merge(new_heap)


    def delete_min(self) -> None:
        '''
        O(log(n))
        '''

        if not self.l: 
            self.root = None 
            self.n = 0

        else:
            left = self.l
            right = self.r

            self.n = left.n
            self.root = left.root

            self.l = left.l
            self.r = left.r

            self.merge(right)


    def empty(self) -> bool:
        return self.n == 0


    def size(self) -> int:
        return self.n

  
    def merge(self, other: 'Optional[LeftistHeap[T]]') -> None:
        '''
        O(log(n))
        '''
        if not other:
            return

        self.n += other.n

        if not self.root:
            self.root = other.root
            return

        if self.min() > other.min():
            self.swap_root(other)
        
        if not self.r: 
            self.r = other
        else:
            self.r.merge(other)

        if self.r and not self.l:
            self.swap_children()

        elif self.r and self.l and self.r.root.s > self.l.root.s:
            self.swap_children()

        if not self.r:
            self.root.s = 0

        else:
            self.root.s = self.r.root.s + 1


    def swap_root(self, other) -> None:
        old_root = self.root
        self.root = other.root
        other.root = old_root


    def swap_children(self) -> None:
        temp = self.l
        self.l = self.r
        self.r = temp


    def preorder(self):
        '''
        O(n)
        '''
        yield self.root.e

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

        yield self.root.e

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

        yield self.root.e


    def pretty_print(self) -> None:
        if not self.root:
            print("Empty")
            return

        self.pretty_print_recursive(0)


    def pretty_print_recursive(self, i) -> None:
        spacer = " " * 2 * i
        print(spacer + str(self.root.e) \
            + ", s=" + str(self.root.s) \
            + ", n=" + str(self.n))
        
        print(spacer + "left:")
        if self.l:
            self.l.pretty_print_recursive(i + 1)
        
        print(spacer + "right:")
        if self.r:
            self.r.pretty_print_recursive(i + 1)

