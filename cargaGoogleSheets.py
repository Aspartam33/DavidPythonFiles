import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def auth_google():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('AutomarizacionTiendas-fca572e81aca.json',scope)

    client = gspread.authorize(creds)

    sheet = client.open('data-prueba')
    csv_to_sheets(sheet,client)
def csv_to_sheets(sheet,client):
    auth_google()
    with open('data.csv','r') as file_obj:
        content = file_obj.read()
        res = client.import_csv(sheet.id, data=content)
        return res

def create_new_sheets(sheet,client):
    auth_google()
    sheet.add_worksheet(rows=1430,cols=2,title='Nombres1')
    sheet_runs = sheet.get_worksheet(1)
    
auth_google()

