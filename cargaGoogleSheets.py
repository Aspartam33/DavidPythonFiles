import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def auth_google():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('AutomarizacionTiendas-506d946c64f0.json',scope)

    client = gspread.authorize(creds)

    sheet = client.open('data-prueba')

    with open('data.csv','r') as file_obj:
        content = file_obj.read()
        client.import_csv(sheet.id, data=content)
auth_google()