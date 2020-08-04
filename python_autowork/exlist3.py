from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(['Number','data'])

for i in range(10):
    ws.append([i, str(i) + 'data'])


wb.save('simple_result.xlsx')