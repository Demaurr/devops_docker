from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = list(User.objects.values('id', 'name', 'dsu_id'))
        return JsonResponse(users, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        dsu_id = data.get('dsu_id')
        user = User.objects.create(name=name, dsu_id=dsu_id)
        return JsonResponse({'id': user.id, 'name': user.name, 'dsu_id': user.dsu_id}, status=201)

    return JsonResponse({'error': 'Method not allowed.'}, status=405)