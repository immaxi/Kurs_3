def field_str(sp, *args):                                       #1
    assert len(args) > 0
    poyasnenie = "\nВыполняется функция field(goods, "
    for i in range (len(args)):
        poyasnenie += (str(args[i]) + ", ")
    poyasnenie = poyasnenie[:-2]
    poyasnenie += "):"
    print(poyasnenie)
    if len(args) == 1:
        stroka = ""
        for element_sp in sp:
            if element_sp[args[0]] != None: 
                stroka += (str(element_sp[args[0]]) + ", ")
        stroka = stroka[:-2]
        print(stroka)
    else:
        slovar = {}
        stroka = ""
        for element_sp in sp:
            for i in range(len(args)):
                if element_sp[args[i]] != None:
                     slovar[args[i]] = element_sp[args[i]]
            stroka += (str(slovar) + ", ")
            slovar.clear()
        stroka = stroka[:-2]
        print(stroka)

def gen_random_str(kolvo, min, max):                           #2
    stroka = ""
    for i in range(kolvo):
        stroka += (str(randint(min, max)) + ", ")
    stroka = stroka[:-2]
    print(stroka)
