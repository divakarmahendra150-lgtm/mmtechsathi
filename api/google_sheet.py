import os
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


def get_google_sheet():
    credentials_path = os.environ.get(
        "GOOGLE_CREDENTIALS_FILE",
        "google-credentials.json",
    )

    credentials = Credentials.from_service_account_file(
        credentials_path,
        scopes=SCOPES,
    )

    client = gspread.authorize(credentials)

    spreadsheet_id = os.environ.get("GOOGLE_SHEET_ID")

    if not spreadsheet_id:
        raise ValueError("GOOGLE_SHEET_ID is not configured.")

    spreadsheet = client.open_by_key(spreadsheet_id)

    return spreadsheet.sheet1


def save_contact_to_sheet(name, email, phone, service, details):
    worksheet = get_google_sheet()

    worksheet.append_row([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        name,
        email,
        phone,
        service,
        details,
    ])

    return True