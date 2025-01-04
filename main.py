import flet as ft
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
import datetime as dt
# python3 -m pip install google-auth
# python3 -m pip install google-api-python-client
# python3 -m pip install google_auth_oauthlib
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:\\Users\\Ricardo R Lima\\Documents\\prog\\Upload_Document_V2\\uploaddocumentv2-01911cd8058b.json'
PARENT_FOLDER_ID = "1dmqBpdV0GwKTJS4gYLR26jYSkbQsfd1q"

def autenticador():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds


def upload(file_path):
    credencial = autenticador()
    service = build('drive', 'v3', credentials=credencial)

    # Obtém o nome do arquivo a partir do caminho
    file_name = file_path.split('/')[-1]

    file_metadata = {
        'name': file_name,  # Definindo o nome do arquivo corretamente
        'parents': [PARENT_FOLDER_ID]
    }

    media = MediaFileUpload(file_path)  # Preparando o arquivo para upload

    file = service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()

    print(f"Upload do arquivo {file_name} concluído com sucesso!")

# Exemplo de uso
upload('C:\\Users\\Ricardo R Lima\\Documents\\prog\\Upload_Document_V2\\asce.jpg')

def main(page: ft.Page):
    page.title = 'New App'
    page.theme_mode = 'dark'
    # Fonts do aplicativo
    page.fonts = {
        "Poppins": "fonts/Poppins-Bold.ttf",
        "Poppins2": "fonts/Poppins-Light.ttf",
        "Poppins3": "fonts/Poppins-Regular.ttf",
        }

    # Efeito SnackBar
    def Snackbar(color: str = "green"):
            page.snack_bar = ft.SnackBar(ft.Text("Teste Pedro napa", color="White",style="Poppins"))
            page.snack_bar.open = True
            page.snack_bar.bgcolor = color
            page.update()
    Snackbar()
    def selecione(e):
        arquivo = filedialog.askopenfilename()
        print(arquivo)
    selectArq = ft.ElevatedButton(
        "Teste",
        on_click=selecione,

        style=ft.ButtonStyle(
            color='white',
            bgcolor='Black',
            overlay_color='Red'
        )
    )
    
    page.add(
       ft.Row([selectArq])
        )


ft.app(main)
