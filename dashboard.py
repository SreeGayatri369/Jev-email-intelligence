import pandas as pd

from gmail_service import get_recent_emails
from jev_service import evaluate_email


def analyze_inbox():

    emails = get_recent_emails(10)

    rows = []

    for email in emails:

        result = evaluate_email(
            email["raw"]
        )

        answers = result["answers"]

        rows.append({

            "Subject":
            email["subject"],

            "Priority Score":
            answers["priority_score"]["score"],

            "Priority Confidence":
            answers["priority_score"]["confidence"],

            "Priority":
            answers["priority_choice"]["choice"],

            "Reply Required":
            answers["reply_required"]["noul"],

            "Action Required":
            answers["action_required"]["noul"],

            "Security Risk":
            answers["security_risk"]["noul"],

            "Customer Impact":
            answers["customer_impact"]["noul"],

            "Category":
            answers["category"]["choice"]
        })

    return pd.DataFrame(rows)