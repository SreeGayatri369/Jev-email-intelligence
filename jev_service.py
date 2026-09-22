import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "TYPESAFE_API_KEY"
)

URL = "https://api.typesafe.ai/v1/systemone"


def evaluate_email(email_text):

    payload = {

        "model": "jev-latest",

        "state": email_text,

        "questions": {

            "priority_score": {

                "type": "score",

                "instructions":
                "How important is this email?",

                "criteria": [

                    "Ignore",

                    "Low",

                    "Medium",

                    "High",

                    "Critical",

                    "INSANE"
                ]
            },

            "priority_choice": {

                "type": "choice",

                "instructions":
                "Choose the priority.",

                "criteria": {

                    "Ignore":
                    "Not useful",

                    "Low":
                    "Can wait",

                    "Medium":
                    "Normal importance",

                    "High":
                    "Important",

                    "Critical":
                    "Urgent business impact",

                    "INSANE":
                    "Immediate action required"
                }
            },

            "reply_required": {

                "type": "noul",

                "instructions":
                "Does this email require a reply?"
            },

            "action_required": {

                "type": "noul",

                "instructions":
                "Does this email require action?"
            },

            "security_risk": {

                "type": "noul",

                "instructions":
                "Does this email indicate a security issue?"
            },

            "customer_impact": {

                "type": "noul",

                "instructions":
                "Does this email impact customers?"
            },

            "category": {

                "type": "choice",

                "instructions":
                "Choose email category.",

                "criteria": {

                    "Production":
                    "Production issue",

                    "Security":
                    "Security topic",

                    "Meeting":
                    "Meeting event",

                    "HR":
                    "HR communication",

                    "Finance":
                    "Billing, invoices, payments",

                    "General":
                    "General communication"
                }
            }
        }
    }

    response = requests.post(

        URL,

        headers={
            "Authorization":
            f"Bearer {API_KEY}",

            "Content-Type":
            "application/json"
        },

        json=payload
    )

    return response.json()