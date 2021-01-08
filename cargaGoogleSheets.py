import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def auth_google():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('AutomarizacionTiendas-fca572e81aca.json',scope)

    client = gspread.authorize(creds)

    sheet = client.open('data-prueba')
   
    nom_file='data.csv'
    with open(nom_file,'r') as file_obj:
        content = file_obj.read()
        res = client.import_csv(sheet.id, data=content)
        return res   
auth_google()

