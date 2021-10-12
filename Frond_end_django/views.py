from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
import json
from Frond_end_django.comparisonHttp import send_shapemodel_request, send_colormodel_request
from Frond_end_django.standard_values import get_standard_values_shape, get_standard_values_color
from Frond_end_django.save_values import save_settings_shape, save_settings_color
from django.contrib.sessions.models import Session

@csrf_exempt
def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    if request.method == 'POST':
        data_from_post = json.load(request)['image']
        data_from_post = data_from_post[22:]
        identifier = 'shape' #Wat is de identifier!?!
        shape = request.session['values']['shape']
        response_shape = send_shapemodel_request(data_from_post, identifier, shape)
        response_color = send_colormodel_request(data_from_post)
        print("Shape is:", response_shape) #Remove this tag, and use the function to show a visual index
        print("Color is:", response_color) #Remove this tag, and use the function to show a visual index
    return HttpResponse(template.render(context, request))

@csrf_exempt
def settings(request):

    if request.session.is_empty():
        shape = get_standard_values_shape()
        color = get_standard_values_color()
        request.session['values'] = {"shape": shape, "color": color}
        values = request.session['values']
    else:
        #Session.objects.all().delete() #If session crash, run this
        values = request.session['values']

    if request.method == 'POST':
        if request.POST.get('action') == 'shape_reset':
            values['shape'] = get_standard_values_shape()
            request.session['values'] = values
        elif request.POST.get('action') == 'color_reset':
            values['color'] = get_standard_values_color()
            request.session['values'] = values

    if request.method == 'POST':
        if request.POST.get('action') == 'shape':
            request.session['values'] = save_settings_shape(request, values)
        elif request.POST.get('action') == 'color':
            request.session['values'] = save_settings_color(request, values)

    print(request.session['values'])

    template = loader.get_template('app/settings.html')
    context = {'form': values}
    return HttpResponse(template.render(context['form']))

def information(request):
    template = loader.get_template('app/information.html')
    context = {}
    return HttpResponse(template.render(context))