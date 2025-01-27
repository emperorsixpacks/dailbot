from __future__ import annotations

import hashlib
import hmac
import os
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from pyairtable.api import Base
    from pyairtable.models.webhook import CreateWebhookResponse


def return_app_dir():
    return os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(path=__file__))


BASE_DIR = os.path.dirname(os.path.abspath(return_app_dir()))


def create_new_webhook(
    airtable_client: Base, webhook_url
) -> Optional[CreateWebhookResponse]:
    for webhook in airtable_client.webhooks():
        if webhook.notification_url == webhook_url:
            return None
    res = airtable_client.add_webhook(
        notify_url=webhook_url,
        spec={
            "options": {
                "filters": {
                    "dataTypes": ["tableData"],
                    "recordChangeScope": "tblZbNhBmDblSUXR1",
                    "changeTypes": ["create", "update", "delete"],
                }
            }
        },
    )
    return res


def write_secret(secret: str):
    with open(os.path.join(BASE_DIR, "secret.txt"), "w") as file:
        file.write(secret)
        file.close()

def read_secret() -> str:
    with open(os.path.join(BASE_DIR, "secret.txt"), "r") as file:
        data = file.read()
        file.close()
        return data


def verify_signature(payload, received_signature):
    computed_signature = hmac.new(
        whatsapp_config.whatsapp_token.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_signature, received_signature)
