answerKey = 'TTFF'
k = 2
n = len(answerKey)
answer_l = list(answerKey)
count = i = 0
while count < k:
    if answer_l[i] == 'F':
        answer_l[i] = 'T'
        count += 1
    i += 1
print(answer_l.count('T'))
