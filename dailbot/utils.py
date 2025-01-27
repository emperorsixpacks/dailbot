from __future__ import annotations

import hashlib
import hmac
import json
import os
from typing import TYPE_CHECKING, Optional

from pyairtable.models.webhook import CreateWebhookResponse

if TYPE_CHECKING:
    from pyairtable.api import Base


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
                    "changeTypes": ["add", "remove", "update"],
                    "fromSources": ["formSubmission"],
                }
            }
        },
    )
    return res


def write_webhook(data: CreateWebhookResponse):
    with open(os.path.join(BASE_DIR, "webhook.json"), "w") as file:
        dict_data = data.model_dump()
        dict_data["expiration_time"] = str(dict_data["expiration_time"])
        json.dump(dict_data, file)
        file.close()


def read_webhook() -> CreateWebhookResponse:
    with open(os.path.join(BASE_DIR, "webhook.json"), "r") as file:
        json_data = json.load(file)
        file.close()
        json_data = CreateWebhookResponse(**json_data)
        return json_data


def verify_signature(webhook_secret, payload, received_signature):
    computed_signature = hmac.new(webhook_secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_signature, received_signature)
