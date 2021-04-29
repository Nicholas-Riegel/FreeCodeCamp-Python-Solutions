
def arithmetic_arranger(List):
    for x in List:
        list0 = x.split(' ')
        a = list0[0]
        b = list0[1]
        c = list0[2]
        if len(a) > len(c):
            prob_len = len(a) + 2
        elif len(c) > len(a):
            prob_len = len(c) + 2
            toplead = prob_len - len(a)
            toprow = str()
            toprow += ' ' * toplead
            toprow += a
            bottomrow = b + ' ' + c
            underscore = '-' * prob_len
        else:
            prob_len = len(a)
    print(toprow)
    print(bottomrow)
    print(underscore)

arithmetic_arranger(["3 + 8808"])
