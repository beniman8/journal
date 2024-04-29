from django_extensions.management.jobs import DailyJob


class SendMailJob(DailyJob):
    help = "sent mail to active accounts"

    def execute(self):
        pass
        # return super().execute()
