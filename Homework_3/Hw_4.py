# 4. Write a program that will convert a decimal number to binary.

number = input('Enter number: ')


def add_binary(a):
    ostatok = a % 2
    delimoe = a//2
    answer = [ostatok]
    while (delimoe > 0):
        ostatok = delimoe % 2
        delimoe = delimoe//2
        answer.append(ostatok)
    answer.reverse()
    answerstring = ''.join(str(e) for e in answer)
    print(answerstring)
    return (answerstring)


print(add_binary(number))
