from collections.abc import Iterable                                            # Iterable-y tip a, vor en popoxakanneri hamar a, voronc vra karas cikl fras for-ov (xosqi list, tuple)

class CollectionTypeError(TypeError):                                           # dzerov sarqac Error a eli, vor mi qani tex ogtagorcvi
    def __init__(self, msg = 'MyNumberCollection supports only numbers!'):
        self.msg = msg
        
    def __str__(self):
        return self.msg
        
class CollectionConcatenationException(Exception):                              # eli dzerov sarqac Error a
    def __init__(self, msg = 'MyNumberCollection supports concatenation only for collections of numbers!'):
        self.msg = msg
        
    def __str__(self):
        return self.msg

def isNumber(value):                                                    # funkcia a vor stugum a ardyoq iran poxancac arjeqy tiv a, te che
    if not isinstance(value, (int, float)):
        return False
    return True

class MyNumberCollection:                                                       # Tvayin arjeqner pahelu classn a mer
    def __init__(self, start = None, end = None, step = 1):                           # stanum a start, end, u qayl. Kara menak start-y poxanci object-y sarqeluc, vory iranic karan nerkayacni Iterable (list, tuple)
        self.collection = []                                                    # ed mer tvayin arjeqnery pahelu enq listi mej
        if isinstance(start, Iterable):                                         # nayum a ete Iterable tipi a
            if all(map(isNumber, start)):                                       # ira bolor tarrery stugum a vor tvayin arjeq linen (map funkcian frum a tarreri vrov u isNumber funkcian a ashxatacnum amen meki hamar u veradarcnum a True)
                self.collection.extend(start)                                   # ete bolory tver en, ed poxancac Iterable-y qcum a collection-i mej
            else:
                raise CollectionTypeError                                       # ete che, mer dzerov sarqac Errorn a dzum
        elif all(map(isNumber, (start, end, step))):                            # esi en depqn a, vor dzerov talis a skizby, verjy u qayly u drancov petq a inqy sarqi tveri range u qci mer collectioni mej
            self.collection.extend(range(start, end + 1, step))                 # sarqel a range-y u qcel a collection-i mej. (end + 1 a arac, vor end-n el mtni collection-i mej)
            
            if end not in self.collection:                                      # esi en depqi hamar a, erb qayly nenc a araj etum, vor end-i vrov trnum a. dra hamar stugum a, ete end-y chka mer collection-i mej, avelacnum a
                self.collection.append(end)

    def __str__(self):                                                          # esi vor uzenas print anes, sirun tpi
        return '{collection}'.format(collection = self.collection)

    def append(self, number):                                                   # esi qo exac collection-in verjic avelacnum a arjeq
        if isNumber(number):                                                    # demic stugum a tiv a te che
            self.collection.append(number)                                      # ete tiv a, avelacnum a
        else:                                                                   # ete che
            raise CollectionTypeError                                           # qcum a mer dzerov sarqac Error-y

    def __add__(self, other):                                                   # esi mer class-i obyektin vor + nshanov uzum en gumar en, dra funkcionaln a
        result = self.collection.copy()                                         # demic mer collection-y copy enq anum, vor copy-i vra ashxatenq
        if isinstance(other, MyNumberCollection):                               # stugum a, ete +-i myus koxmum eli nuyn mer class-i tipi objectn a
            result.extend(other.collection)                                     # copyi vra avelacnum enq mer objecti collection-y (mer objecti vra hastat ka)
            return MyNumberCollection(result)                                   # veradarcnum enq taza object arden verjnakan arjeqov. Mer ed pahi objecty nuynn a mnacel
        elif isinstance(other, Iterable):                                       # ste stugum a ete Iterable tipi a
            if all(map(isNumber, other)):                                       # nuyn sxemayov, saxi vrov frum a tenum a ete tver en
                result.extend(other)                                            # avelacnum copyi mej
                return MyNumberCollection(result)                               # u veradarcnum eli mer tipi object verjnakan arjeqnerov
            else:                                                               # ete inch vor mi haty tiv chi linum
                raise CollectionConcatenationException                          # tpum a mer dzerov sarqac 2rd Errory
        else:       
            raise CollectionConcatenationException                              # isk stex ete voch en a, voch en 
    
    __radd__ = __add__                                                          # esi arac a, vor +-i erku koxmeric el ylni mer objecty grel

    def __getitem__(self, index):                                               # esi indexov vercum a mer objectiv arjeqy
        return self.collection[index] ** 2                                      # u barcracnum qarakusi nor veradarcnum (yst pahanji)

    def __iter__(self):                                                         # esi Iterable-i paddzerjken a
        self.index = - 1                                                        # index-y dnum a -1-i vra (nerqevy kasem xi)
        return self

    def __next__(self):                                                         # esi amen hajord tarn a veradarcnum (cikl fralu hamar a petq, mek el vor dzerov kanchum es nex() funkcian)
        if self.index < len(self.collection) - 1:                               # nayum a qani der indexy verjin chi hasel (verj - 1, vorovhetev -1-ic einq sksel)
            self.index += 1                                                     # indexin gumarum a 1
            return self.collection[self.index]                                  # u veradarcnum mer listic indexov arjeqy. Ay stea erevum te xi enq demic tvel -1. Vor araji qayli vaxt sarqi index-y 0 u veradarcni arajin tarry. Veradarcneluc heto el chenq kara grenq index + 1. Dra hamar senc a arvum
        else:
            raise StopIteration                                                 # henc hasnum a verjin, stop a talis fraly


col1 = MyNumberCollection(0, 5, 2)
print(col1)

col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2)

try:
    col3 = MyNumberCollection((1, 2, 3, "4", 5))
except CollectionTypeError as msg:
    print(msg)

col1.append(7)
print(col1)

try:
    col2.append("string")
except CollectionTypeError as msg:
    print(msg)

print(col1 + col2)
print(col1 + [1, 4, 5, 8, 9])

try:
    print(col1 + "[1, 4, 5, 8, 9]")
except CollectionConcatenationException as msg:
    print(msg)

print(col2[4])