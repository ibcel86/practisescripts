import os
import openpyxl


script_dir = os.path.dirname(os.path.abspath(__file__))

folder = os.path.join(script_dir, 'Data')
output_file = os.path.join(script_dir, 'Data', 'masterfile.xlsx')

output_wb = openpyxl.Workbook()
output_sheet = output_wb.active
output_sheet.title = "Test Data"

cells = ['A2', 'B2']

for filename in os.listdir(folder):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder, filename)
        wb = openpyxl.load_workbook(file_path)
        # Make sure to select the right worksheet, change index if necessary
        wb.active = wb.worksheets[1]
        values = [wb.active[cell].value for cell in cells]
        output_sheet.append(values)

output_wb.save(output_file)



