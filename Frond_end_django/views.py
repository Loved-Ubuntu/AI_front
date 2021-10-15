from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from Frond_end_django.comparisonHttp import *
from Frond_end_django.standard_values import get_standard_values_shape, get_standard_values_color, check_for_session
from Frond_end_django.save_values import save_settings_shape, save_settings_color
from django.contrib.sessions.models import Session

@csrf_exempt
def index(request):
    models = json.loads(get_models())
    # print(models['message'][0]['imageOperations']) #settings (loop the 0)
    # print(models['message'][0]['hist']) #image
    #print(models['message'][0]['identifier'])  # model_name

    #print(models)
    try:
        response
    except NameError:
        response = {'shape': 'None', 'color': 'None', 'label': 'Yet to implement'}
    if request.method == 'POST':
        if request.POST.get('action') == 'send_image':
            data_from_post = request.POST.get('image')
            request.session['image'] = data_from_post[22:]

        if request.POST.get('action') == 'post_image':
            data_from_post = request.session['image']
            model = "ex3_modelx"  # Dit moet opgevraagd worden  #For make model
            shape = request.session['values']['shape'] #For make model
            color = request.session['values']['color'] #For make model
            identifier = 'ex3_model_shape'  # Make session to select model
            response_color = json.loads(send_color_request(data_from_post, identifier))
            response_shape = json.loads(send_shape_request(data_from_post, identifier))
            print(response_shape)

            if response_shape['type'] == "error":
                print(response_shape['message'])
                response['shape'] = "Error"
            elif response_shape['type'] == "true":
                response['shape'] = "Accepted"
            elif response_shape['type'] == "false":
                response['shape'] = "Denied"

            if response_color['type'] == "error":
                print(response_shape['message'])
                response['color'] = "Error"
            elif response_color['type'] == "true":
                response['color'] = "Accepted"
            elif response_color['type'] == "false":
                response['color'] = "Denied"

        if request.POST.get('action') == 'new_model':
            values = check_for_session(request)
            print(values)
            # Set vars
            modelimg = request.session['image']
            model_name = request.POST.get('model_name')
            # Create models
            print('send_shapemodel_request...')
            response_shapemodel_request = send_shapemodel_request(modelimg, model_name + '_shape', values['shape'])
            print('send_colormodel_request...')
            response_colormodel_request = send_colormodel_request(modelimg, model_name + '_color', values['color'])
            print("Response from shape: ", response_shapemodel_request)
            print("Response from color: ", response_colormodel_request)

    template = loader.get_template('app/index.html')
    context = {'models': models, 'response': response}
    #for key in models['message']:
        #print(key['identifier'])
        #print(key)
    return HttpResponse(template.render(context, request))

@csrf_exempt
def settings(request):
    values = check_for_session(request)

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

    #print(request.session['values']) # To see if session is correct

    template = loader.get_template('app/settings.html')
    context = {'form': values}
    return HttpResponse(template.render(context['form']))

def information(request):
    template = loader.get_template('app/information.html')
    context = {}
    return HttpResponse(template.render(context))