import xlwings as xw

# 엑셀파일을 다루기 위해 인스턴스를 생성 = 실제로 엑셀파일이 열려짐
wb = xw.Book('deid_sample.xlsx')

# 엑셀파일 인스턴스로부터 시트 인스턴스를 얻는 3가지 방법
#시트명  sheet1 = wb.sheets['Sheet1']
#방법2
sheet2 = wb.sheets['Sheet2']

# printing names of sheets
sheet_names = []
for sheet in wb.sheets:
    sheet_names.append(sheet.name)

print("Names of sheets:")
for i, sheet_name in enumerate(sheet_names, 1):
    print(f"{i}. {sheet_name}")