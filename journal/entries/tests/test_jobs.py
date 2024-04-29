from journal.entries.jobs import SendMailJob


class TestSendMailJob:
    def test_send_email(self):
        """An active account receive an email propmt"""
        # user = UserFactory()
        job = SendMailJob()

        job.execute()

        # assertion on the outbox
