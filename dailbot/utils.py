from __future__ import annotations

import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyairtable.api import Base


def return_app_dir():
    return os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(path=__file__))


def create_new_webhook(airtable_client: Base, webhook_url):
    for webhook in airtable_client.webhooks():
        if webhook.notification_url == webhook_url:
            return
    airtable_client.add_webhook(
        notify_url=webhook_url,
        spec={
            "options": {
                "filters": {
                    "dataTypes": ["tableData"],
                    "recordChangeScope": "tblZbNhBmDblSUXR1",
                }
            }
        },
    )


BASE_DIR = os.path.dirname(os.path.abspath(return_app_dir()))
