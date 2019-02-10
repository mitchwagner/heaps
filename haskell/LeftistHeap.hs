module LeftistHeap
( Heap
, rank
, isEmpty
, makeHeap
, merge
, insert
, findMin 
, deleteMin 
) where


data Heap a = E | T Int a (Heap a) (Heap a) deriving (Show)


rank :: Heap a -> Int
rank E = 0
rank (T r _ _ _) = r


isEmpty :: Heap a -> Bool
isEmpty E = True
isEmpty _ = False


makeHeap :: a -> Heap a -> Heap a -> Heap a
makeHeap x a b =
    if rank a > rank b then T (rank b + 1) x a b
    else T (rank a + 1) x b a


merge :: Ord a => Heap a -> Heap a -> Heap a
merge h E = h
merge E h = h
merge h1@(T r1 x a1 b1) h2@(T r2 y a2 b2) =
    if x < y then makeHeap x a1 (merge b1 h2)
    else makeHeap y a2 (merge b2 h1)


insert :: Ord a => a -> Heap a -> Heap a
insert x h = merge h (makeHeap x E E)


findMin :: Heap a -> a
findMin E = error "Empty heap"
findMin (T _ x _ _ ) = x


deleteMin :: Ord a => Heap a -> Heap a
deleteMin E = error "Empty heap"
deleteMin (T _ _ a b) = merge a b


instance Functor Heap where
    fmap f E = E
    fmap f (T r x a b) = T r (f x) (fmap f a) (fmap f b)
