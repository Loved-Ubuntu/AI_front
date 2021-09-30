from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))