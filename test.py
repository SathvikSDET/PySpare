import openpyxl
import os

# Correct file path without the extra 'PySpare' folder
file_path = os.path.join(os.getcwd(), "tests", "test-data", "Opencart_LoginData.xlsx")

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at: {file_path}")

# Load the workbook
workbook = openpyxl.load_workbook(file_path)

# Get the active sheet
sheet = workbook.active

# Function to get a cell value
def get_cell_value(row, column):
    return sheet.cell(row=row, column=column).value

# Example usage
if __name__ == '__main__':
    try:
        # Retrieve and print the value of cell (2, 2)
        value = get_cell_value(2, 2)
        print(f"Value at (2, 2): {value}")
    except Exception as e:
        print(f"An error occurred: {e}")
