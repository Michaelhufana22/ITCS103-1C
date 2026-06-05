import openpyxl as op
    
workbook = op.Workbook()
sheet = workbook.active


sheet['A1'] = "Name"
sheet['B1'] = "Room"
sheet['C1'] = "Contact"
sheet['D1'] = "Movein"
sheet['E1'] = "Rent"
sheet['F1'] = "Status"

workbook.save("HUFANA_Database.xlsx")