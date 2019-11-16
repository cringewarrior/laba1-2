letters1 = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
letters1 += letters1
letters2 = 'abcdefghijklmnopqrstuvwxyz'
letters2 += letters2
letters3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters3 += letters3
letters4 = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯ'
letters4 += letters4
digits = '0123456789'
step1 = 2
step2 = 2

while True:
    text = input("Please write your text: ")
    d = ''
    result = ''
    text += ' '
    for a in text:
        if a in digits:
            d += str(a)
        else:
            if d:
                result += str(int(d) + step2)
                d = ''
            if a in letters1:
                res = letters1[letters1.index(a) + step1]
            elif a in letters2:
                res = letters2[letters2.index(a) + step1]
            elif a in letters3:
                res = letters3[letters3.index(a) + step1]
            elif a in letters4:
                res = letters4[letters4.index(a) + step1]
            else:
                res = a
            result += res
    print(result)