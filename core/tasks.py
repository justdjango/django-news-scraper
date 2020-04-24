from celery import shared_task, task

# allows you to call this function asynchronously
@shared_task
def send_mass_emails(recipient):
    print("Doing it")


@task
def send_scheduled_emails():
    # get all those email addresses
    pass
