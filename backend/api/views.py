import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request ->instance of  HttpRequest -> of Django
    # request.body

    body = request.body  # byte string of JSON data
    print(request.body, "body is empty?")
    data = {}
    try:
        data = json.loads(body)  # string of JSON data -> Python Dictionary
    except:
        pass
    # print(body)
    # print("url params: ", request.GET)  # url query paramss
    data["headers"] = dict(request.headers)
    data["content-type"] = request.content_type
    data["params"] = request.GET
    # print(data)

    return JsonResponse(data)
