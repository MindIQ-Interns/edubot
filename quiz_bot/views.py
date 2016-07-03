from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import BotUser
from .serializers import BotUserSerializer


class BotUserData(APIView):

    def get(self, request, pk, format=None):
        try:
            bot_user = BotUser.objects.get(pk=pk)
            serializer = BotUserSerializer(bot_user)
            return Response(serializer.data)

        except BotUser.DoesNotExist:
            raise Http404
