from .models import BotUser


class QuizBot:

    def __init__(self, fb_id):
        try:
            self.client_data = BotUser.objects.get(fb_id=fb_id)
            self.mode = 'home'

        except BotUser.DoesNotExist:
            self.client_data = BotUser()
            self.mode = 'register'

    def register(self):
