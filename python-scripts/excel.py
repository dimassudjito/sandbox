import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
wb.get_sheet_names()