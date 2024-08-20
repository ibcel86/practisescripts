import os
import openpyxl

folder = "D:\My Documents\Code\Data"
output_file = "D:\My Documents\Code\Data\masterfile.xlsx"

output_wb = openpyxl.Workbook()
output_sheet = output_wb.active
output_sheet.title = "Test Data"

cells = ['A2', 'B2']

for filename in os.listdir(folder):
    if filename.endswith('.xlsx'):
        filename = os.path.join(folder, filename) 
        wb = openpyxl.load_workbook(filename)
        wb.active = wb.worksheets[1]
        values = [wb.active[cell].value for cell in cells]
        output_sheet.append(values)

output_wb.save(output_file)



