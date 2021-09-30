from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
import json
from Frond_end_django.ShapeComparisonHttp import send_image

@csrf_exempt
def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    if request.method == 'POST':
        data_from_post = json.load(request)['image']
        response = send_image(data_from_post)
        print(response)
    return HttpResponse(template.render(context, request))