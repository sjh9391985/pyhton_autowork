datafile =open('data2.txt', 'a', encoding='utf-8')
user_input = input("Input: ")
datafile.write(user_input + '\n')
datafile.close()