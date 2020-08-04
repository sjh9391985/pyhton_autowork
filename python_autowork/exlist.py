data = []

for i in range(10):
    data.append(['data1', 'data2', 'data3'])

csvfile = open('result csv', 'w', encoding='utf-8')

for row in data:
    row_str = ','.join(row)
    csvfile.write(row_str + '\n')

csvfile.close()