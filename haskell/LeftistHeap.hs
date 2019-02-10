module LeftistHeap (LeftistHeap) where
import Heap

data LeftistHeap a = E | T Int a (LeftistHeap a) (LeftistHeap a)
    deriving (Show)


rank :: LeftistHeap a -> Int
rank E = 0
rank (T r _ _ _) = r


makeHeap x a b =
    if rank a > rank b then T (rank b + 1) x a b
    else T (rank a + 1) x b a


instance Heap LeftistHeap where
    isEmpty E = True
    isEmpty _ = False

    merge h E = h
    merge E h = h
    merge h1@(T r1 x a1 b1) h2@(T r2 y a2 b2) =
        if x < y then makeHeap x a1 (merge b1 h2)
        else makeHeap y a2 (merge b2 h1)

    insert x h = merge h (makeHeap x E E)

    findMin E = error "Empty heap"
    findMin (T _ x _ _ ) = x

    deleteMin E = error "Empty heap"
    deleteMin (T _ _ a b) = merge a b


instance Functor LeftistHeap where
    fmap f E = E
    fmap f (T r x a b) = T r (f x) (fmap f a) (fmap f b)
