def endless_fib_generator():                                        # fibonacii hamar hajordakanutyun a
    prevValue = 0                                                   # skzbi arjeqy talis enq 0
    curValue = 1                                                    # hajord arjeqy talis enq 1
    while True:                                                     # eli anverj katarvelu a
        curValue += prevValue                                       # hajord arjeqin gumarum a naxord arjeqy
        prevValue = curValue - prevValue                            # naxord arjeqin veragrum a ed pahi arjeqy
        yield prevValue                                             # u veradarcnum a naxordy
                                                                    # senc stacvum a araji qayli vaxt (1, 1) u veradarcnum a araji 1-y. Hajord qayli vaxt darnum a (1,2) u veradarcnum a eli araji arjeqy, aysinqn eli 1. hajord qayli vaxt darnum a (2,3) u eli veradarcnum a araji arjeqy, aysinqn 2 u tenc sharunak

gen = endless_fib_generator()
for i in range(100):
    print(next(gen), end=' ')
