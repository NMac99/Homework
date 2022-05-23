class EvenRange:                                                # esi petq a mez ta eli Iterable, vory kveradarcni mer tvac sahmannerum zuyg tvery
    def __init__(self, start, end):                   # stanum a skizby u verjy
        self.end = end                                          # objecti vra nstcnum enq verjy
        if start % 2 == 0:                                      # u nayum enq, ete skizby zuyg a, henc iran enq nstcnum vorpes objecti skizb 
            self.index = start
        else:                                                   # ete che, ira hajord tivn enq nstcnum, vorovhetev ete inqy kent er, hajordy hastat zuyg a
            self.index = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.end:                              # qani der index-y poqr a verjic
            self.index += 2                                     # 2 hatov avelacnum enq (vor zuygerov gna)
            return self.index - 2                               # u veradarcnum enq index - 2 (vorovhetev stex en -1-i principov chenq skizby tvel amenademic, dra hamar mi hat gumarum enq, heto hanum veradarcnelu vaxt)
        else:
            print('"Out of numbers!"')                          # henc hasnum a verjin mi hat tpum a
            raise StopIteration                                 # heto nor stop a talis


myRange = EvenRange(1, 11)
for number in myRange:
    print(number, end = ' ')
yourRange = EvenRange(7, 11)
print(next(yourRange))
print(next(yourRange))
print(next(yourRange))
