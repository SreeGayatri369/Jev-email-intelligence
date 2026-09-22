from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import os

# Absolute project path
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CREDENTIALS_FILE = os.path.join(
    BASE_DIR,
    "credentials.json"
)

TOKEN_FILE = os.path.join(
    BASE_DIR,
    "token.json"
)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify"
]


def get_gmail_service():

    creds = None

    print("Current Directory:", BASE_DIR)
    print("Credentials File:", CREDENTIALS_FILE)
    print("Exists:", os.path.exists(CREDENTIALS_FILE))

    if os.path.exists(TOKEN_FILE):

        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

    if not creds or not creds.valid:

        if (
            creds
            and creds.expired
            and creds.refresh_token
        ):

            creds.refresh(Request())

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )

            creds = flow.run_local_server(
                port=0
            )

        with open(
            TOKEN_FILE,
            "w"
        ) as token:

            token.write(
                creds.to_json()
            )

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service


def get_recent_emails(max_results=10):

    service = get_gmail_service()

    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            maxResults=max_results
        )
        .execute()
    )

    messages = results.get(
        "messages",
        []
    )

    emails = []

    for msg in messages:

        message = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=msg["id"]
            )
            .execute()
        )

        subject = "No Subject"

        headers = message["payload"].get(
            "headers",
            []
        )

        for header in headers:

            if header["name"] == "Subject":

                subject = header["value"]

        emails.append(
            {
                "id": msg["id"],
                "subject": subject,
                "raw": str(message)
            }
        )

    return emails