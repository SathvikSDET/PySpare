import openpyxl
import os

class Excel_helper():
    def __init__(self):
        self.file_path = os.path.join(os.getcwd(), "tests", "test-data", "Opencart_LoginData.xlsx")
        self.workbook = openpyxl.load_workbook(self.file_path)
    
    def get_sheet_(self):
        return self.workbook.active
    
    def get_cell_value(self, row, column):
        return self.get_sheet_().cell(row=row, column=column).value
if __name__ == '__main__':
    excel = Excel_helper()
    print(excel.get_cell_value(2, 2))