def foo(a):
    cont = a.read()
    ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(cont)
    stroka = 0
    slova = 0
    letter = 0
    for line in cont.split('\n'):
        stroka += 1
        slova += len(line.split())
        for word in line.split():
            l=list(word)
            for i in l:
                if i in ascii_letters:
                    letter += 1
    print(stroka, slova, letter)

file=open("asd.txt", "r")
foo(file)