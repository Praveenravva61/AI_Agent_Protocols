import os

import google.auth
import google.auth.credentials
import google.auth.transport.requests
from dotenv import load_dotenv
from google.auth import impersonated_credentials
from google.oauth2 import service_account

def authenticate(location: str | None = None):
    import google.auth
    import os

    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    os.environ["GOOGLE_CLOUD_PROJECT"] = project_id

    if location:
        os.environ["GOOGLE_CLOUD_LOCATION"] = location

    return credentials, project_id