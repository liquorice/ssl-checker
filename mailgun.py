import os
import requests


def send_email(hostname, days, expiry):
    """Send email about expired domain."""
    MG_KEY = os.environ.get("MG_KEY")

    requests.post(
        'https://api.mailgun.net/v3/mg.liquorice.net.au/messages',
        auth=('api', MG_KEY),
        data={
            "from": "software@liquorice.com.au",
            "to": ["hammy@liquorice.com.au"],
            "text": f"{hostname} expires in {days} days on {expiry}",
            "subject": "SSL Cert expiring soon"
        }
    )
