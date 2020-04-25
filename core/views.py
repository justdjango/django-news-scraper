from django.shortcuts import render
from core.tasks import send_mass_emails


def mass_email_view(request):
    recipient = 'fuewhfuew@fewfe.com'
    print("Received request")
    send_mass_emails.delay(recipient)
    return render(request, "index.html")
