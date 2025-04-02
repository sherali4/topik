import openpyxl

# Load the Excel file
workbook = openpyxl.load_workbook('baza.xlsx')

# Select the active sheet or a specific sheet
sheet = workbook.active  # or workbook['SheetName'] if you know the sheet name

# Get the value of cell B4
value_b4 = sheet['B4'].value

# Print the value
print(f"The value in cell B4 is: {value_b4}")
