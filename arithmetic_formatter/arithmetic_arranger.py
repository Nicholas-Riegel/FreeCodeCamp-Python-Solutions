def arithmetic_arranger(List, want_answer=False):
    if len(List) > 5:
        return "Error: Too many problems."
    total_toprow = str()
    total_bottomrow = str()
    total_underscore = str()
    total_answer = str()
    for x in List:
        list0 = x.split(' ')
        a = list0[0]
        b = list0[1]
        c = list0[2]
        if b != '+' and b != '-':
            return "Error: Operator must be '+' or '-'."
        if len(a) > 4 or len(c) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        try:
            int(a) and int(c)
        except:
            return 'Error: Numbers must only contain digits.'
        if len(a) > len(c):
            prob_len = len(a) + 2
            toprow = str()
            toprow = '  ' + a
            bottomrow = b + (' ' * (len(a) - len(c) + 1)) + c
            underscore = '-' * prob_len

            if b == '+':
                answer = str(int(a) + int(c))
            else:
                answer = str(int(a) - int(c))

            answer_lead = prob_len - len(answer)
            answer = ' ' * answer_lead + answer

        elif len(c) > len(a):
            prob_len = len(c) + 2
            toplead = prob_len - len(a)
            toprow = str()
            toprow += ' ' * toplead
            toprow += a
            bottomrow = b + ' ' + c
            underscore = '-' * prob_len

            if b == '+':
                answer = str(int(a) + int(c))
            else:
                answer = str(int(a) - int(c))

            answer_lead = prob_len - len(answer)
            answer = ' ' * answer_lead + answer

        else:
            prob_len = len(a)+2
            toprow = '  ' + a
            bottomrow = b + ' ' + c
            underscore = '-' * prob_len

            if b == '+':
                answer = str(int(a) + int(c))
            else:
                answer = str(int(a) - int(c))

            answer_lead = prob_len - len(answer)
            answer = ' ' * answer_lead + answer

        total_toprow += ' ' * 4 + toprow
        total_bottomrow += ' ' * 4 + bottomrow
        total_underscore += ' ' * 4 + underscore
        total_answer += ' ' * 4 + answer

    arranged_problems = total_toprow[4:] + '\n' + total_bottomrow[4:] + '\n' + total_underscore[4:]

    if want_answer == True:
        arranged_problems += '\n' + total_answer[4:]

    return arranged_problems

print(arithmetic_arranger(
    [
        "1 + 9999",
        "-999 - 9999",
        "45 + 43",
        "1235 + 49",
        "2 + 2"
    ], True)
)
