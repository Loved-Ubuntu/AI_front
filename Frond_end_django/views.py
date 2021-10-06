from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
import json
from Frond_end_django.comparisonHttp import send_image_color, send_image_shape

@csrf_exempt
def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    if request.method == 'POST':
        data_from_post = json.load(request)['image']
        response_shape = send_image_shape(data_from_post)
        response_color = send_image_color(data_from_post)
        print(response)
    return HttpResponse(template.render(context, request))