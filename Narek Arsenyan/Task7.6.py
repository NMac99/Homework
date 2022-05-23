class MyException(Exception):
    def __init__(self, msg = ''):
        self.msg = msg

    def __str__(self):
        return self.msg


class BoolException(MyException):
    pass

class StringException(MyException):
    pass

class TypeException(MyException):
    pass

class EmptyException(MyException):
    pass


def isEven(num = None):
    if num is None:
        raise EmptyException('One argument required')
    elif isinstance(num, str):
        raise StringException('Got string argument. Argument must be integer')
    elif isinstance(num, bool):
        raise BoolException('Got boolean argument. Argument must be integer')
    elif not isinstance(num, int):
        raise TypeException('Unsupported argument type. Argument must be integer')

    return num % 2 == 0
    
def isPrime(num = None):                                                   # stugum a ardyoq tiv-y parz a, te che
    if num == None:                                                                     # eli mer dzerov sarqac Error-nern a ogtagorcum
        raise EmptyException('One argument required')
    if not isinstance(num, int):                                                        # isinstance-y stugum a ardyoq arjeqy patkanum a konkret tipi, te che
        raise TypeException('Unsupported argument type. Argument must be integer')
    if num < 2:                                                                         # 2-ic poqr tvery parz chen
        return False
    
    for i in range(2, num):                                                             # tvi parzutyuny stugox cikln a
        if num % i == 0:                                                                # ete 2-ic minchev ed tivy mijakayqum inchvor tvi vra bajanvum a
            return False                                                                # uremn parz chi
    return True                                                                         # ete ciklic durs a galis ira xodov, voch te en if-ov, uremn voch mi tvi vra chi bajanvel

def primesList(end = None):                                                # 2-ic minchev poxancac tivy sarqum a parz tveri list
    if end == None:
        raise EmptyException('One argument required')
    if not isinstance(end, int):
        raise TypeException('Unsupported argument type. Argument must be integer')
        
    primeValues = []                                                                    # demic datark list enq pahum
    for i in range(2, end + 1):                                                         # heto hertov frum enq tveri vrov
        if isPrime(i):                                                                  # ete parz a
            primeValues.append(i)                                                       # avelacnum enq listi mej
    return primeValues                                                                  # u veradarcnum

def goldbach(num):                                                         # yst goldbachi (mi qich popoxac a arden 21-rd darum kanony), 2-ic mec cankacac zuyg tiv kareli a nerkayacnel 2 parz tveri gumari tesqov
    if num == None:                                                                     # es funkcian gtnum a ed 2 parz tvery
        raise EmptyException('One argument required')
    if not isinstance(num, int):
        raise TypeException('Unsupported argument type. Argument must be integer')
        
    if num > 2 and isEven(num):                                                         # ete tivy mec a 2-ic u zuyg a
        primes = primesList(num)                                                        # gtnum a minchev ed tivy bolor parz tvery
        gValue = [num]                                                                  # mi hat list enq sarqum, vori mej arajin arjeqy mer tivn a, heto avelacnelu enq en erku tvery, voronq ham parz en, ham el iranc gumary talis a mer poxancac tivy
        for i in primes:                                                                # frum enq parz tveri vrov
            if isPrime(num - i):                                                        # ete mer poxancac tvic hanum enq hertakan parz tivy u ed tivn el a linum parz, uremn mer uzac zuygy gtel enq
                gValue.append([i, num - i])                                             # mer listi mej avelacnum enq ed erku tvery arandzin listi tesqov
                return gValue                                                           # u veradarcnum
    else:
        raise MyException('Argument is not supported. Please read homework')            # ete 2 a, kam 2-ic poqr a kam kent tiv a, barcracnum enq es Error-y, vor heto brnenq cragri mej
        
def userInput():                                                                        # funkcia a, vor terminali mej spasum a user-i arjeq nermucelun
    return input('Find goldbach representation of number by entering number. Press "q" to quit:\n')


def consoleProgram():                                                                   # mer cragirn a arden, vor user-in asel a nermuci, inqy hashvi u tpi ardyunqy
    while True:                                                                         # cragiry ashxatelu a enqan, minchev user-y chnermuci "q" tary
        inputValue = userInput()                                                        # kardum a user-i nermucacy
        if inputValue == 'q':                                                           # ete "q" a, durs a galis ciklic u ham el cragric
            print('You quitted program. Bye-bye')                                       # es namaky tpelov
            return
        else:                                                                           # hakarak depqum
            try:
                number = int(inputValue)                                                # porcum a int-i konvert ani, vorovhetev nermucumy string a veradarcnum
            except:
                number = inputValue                                                     # ete chi karum henc ed arjeqn el dnum a mejy. Arden tiperi anhamapatasxanutyan pahy nerqevy kbrnvi
    
            try:
                print(goldbach(number))                                                 # porcum a gtni nermucac tvi hamar parz tveri zuygy
            except MyException as msg:                                                  # ete hashvox funkcian Error a barcracrel ashxatanqi yntacqum (mer sarqac Error-neri masin a xosqy)
                print('Error: {msg}'.format(msg = msg))                                 # ed Error-y tpum a terminalum
            except Exception:                                                           # ete nenc Error a exel, vor mer dzerov grac Error-y chi
                print('Something went wrong')                                           # tpum a es stringy

consoleProgram()                                                                        # ashxatacnum a es cragiry