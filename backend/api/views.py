import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}

    # serializing our data
    # taking our model instance
    # and turning it into a python dictionary
    # we can read properties of instance
    # but that's not dicionary
    # whose property we can read also
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price

    return JsonResponse(data)
