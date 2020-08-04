datafile =open('data.txt', 'r', encoding='utf-8')

line = 'init'
while line:
    line = datafile.readline()
    print(line.strip())

datafile.close()