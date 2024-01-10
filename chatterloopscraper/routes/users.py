from django.http import JsonResponse
from ..models.models import Chatterloopusers
from ..helpers.serializers import UsersSerializer

def users_list(request):

    users = Chatterloopusers.objects.all()
    serializer = UsersSerializer(users, many=True)
    return JsonResponse({ "status": True, "result": serializer.data }, safe=False)