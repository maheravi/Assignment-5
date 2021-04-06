# init
print('loading...')

f = open('Trans/translate.txt')

big_text = f.read()

parts = big_text.split('\n')
# print(parts)
words = []
i = 0
while i < len(parts):
    my_dic = {'english': parts[i], 'persian': parts[i + 1]}
    words.append(my_dic)
    i += 2

# for i in range(len(words)):
#     print(words[i])

print('data loaded')
print('welcome dear user, please enter your text')

while True:
    print()
    print('1- Add new words to Dictionary', '\n2- English to Perasian Translate', '\n3- Persian to English Translate',
          '\n4- Exit')
    m = int(input('Choose your action= '))

    if m == 1:
        eng = input('please enter English word= ')
        per = input('please enter Persian Translate= ')
        my_dic = {'english': eng, 'persian': per}
        words.append(my_dic)
        f = open('Trans/translate.txt','a')
        f.write('\n'+eng)
        f.write('\n' + per)
        f.close()
        print('your word is added to dictionary')


    elif m == 2:
        user_string = input('Please enter your sentence in English= ')

        user_sentence = user_string.split('.')
        # user_words = user_string.split(' ')
        # print(user_words)
        for k in range(len(user_sentence)):
            user_sen = user_sentence[k]
            user_words = user_sen.split(' ')
            for j in range(len(user_words)):
                for i in range(len(words)):
                    if words[i]['english'] == user_words[j]:
                        print(words[i]['persian'], end=' ')
                        break

                else:
                    print(user_words[j], end=' ')

    elif m == 3:
        user_string = input('Please enter your sentence in Persian= ')

        user_sentence = user_string.split('.')
        # user_words = user_string.split(' ')
        # print(user_words)
        for k in range(len(user_sentence)):
            user_sen = user_sentence[k]
            user_words = user_sen.split(' ')
            for j in range(len(user_words)):
                for i in range(len(words)):
                    if words[i]['persian'] == user_words[j]:
                        print(words[i]['english'], end=' ')
                        break

                else:
                    print(user_words[j], end=' ')
    elif m == 4:
        exit()
