from random import randint

with open('vocabulary.txt','r',encoding='utf-8') as vocabulary:
    en, ko = [], []
    for line in vocabulary:
        print(line)
        en.append(line.strip().split(": ")[0])
        ko.append(line.strip().split(": ")[1])

    print(en)
    print(ko)

    while True:
        random_index = randint(0, len(ko)-1)
        answer = input("{}: ".format(ko[random_index]))
        if answer == 'q':
            break
        else:
            if answer == en[random_index]:
                print('맞았습니다!\n')
            else:
                print('틀렸습니다. 정답은 {}입니다.\n'.format(en[random_index]))
