class MySquareIterator:                                             
    def __init__(self, collection):                                 # stanum a Iterable (list, tuple)
        self.collection = collection                                # pahum a objecti vra
        self.index = -1                                             # eli skizby dnum a -1-i vra

    def __iter__(self):                                             # esi Iterable-i paddzerjken a
        return self

    def __next__(self):                                             # amen hajord tary vercnelu paddzerjken a
        if self.index < len(self.collection) - 1:                   # qani der durs chi ekel sahmanic
            self.index += 1
            return self.collection[self.index] ** 2                 # veradarcnum a arjeqi qarakusin
        else:
            raise StopIteration                                     # henc durs a galis, kaynacnum a ira vra fraly

itr = MySquareIterator([1, 2, 3, 4, 5])
for item in itr:
    print(item, end = " ")
