import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Trial automate sheet").sheet1

state = sheet.col_values(5)
pprint(state)
cell = 5
# pprint(state)
for index, value in enumerate(state):
    if value == "State":
        row_number = index + 1
        col_number = cell + 1
        sheet.update_cell(row_number, col_number, "Region")
    if value in ["Haryana", "Punjab", "Delhi", "Rajasthan"]:
        row_number = index+1
        col_number = cell + 1
        sheet.update_cell(row_number, col_number, "Northen india")
    elif value in ["Karnataka", "Kerala", "Tamilnadu", "Hyderabad", "Chennai"]:
        row_number = index + 1
        col_number = cell + 1
        sheet.update_cell(row_number, col_number, "Southern india")
    elif value in ["Gujarat", "Maharashtra", "Goa"]:
        row_number = index + 1
        col_number = cell + 1
        sheet.update_cell(row_number, col_number, "Western india")
    elif value in ["M.P", "U.P"]:
        row_number = index + 1
        col_number = cell + 1
        sheet.update_cell(row_number, col_number, "Central india")
    elif value not in ["Haryana", "Punjab", "Delhi", "Rajasthan","Karnataka", "Kerala", "Tamilnadu", "Hyderabad", "Chennai",
                       "Gujarat", "Maharashtra", "Goa", "M.P", "State", "U.P"]:
        row_number = index + 1
        col_number = cell + 1
        sheet.update_cell(row_number, col_number, "Invalid State")










