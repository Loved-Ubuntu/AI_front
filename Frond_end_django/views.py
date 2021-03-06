from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from Frond_end_django.comparisonHttp import *
from Frond_end_django.standard_values import get_standard_values_shape, get_standard_values_color, check_for_session
from Frond_end_django.save_values import save_settings_shape, save_settings_color

@csrf_exempt
def index(request):
    models = json.loads(get_models())

    #Bij eerste aankomt op site, zijn er nog geen resposes voor in de tabel
    try:
        response
    except NameError:
        response = {'shape': {'class': 'warning', 'type': 'None'}, 'color': {'class': 'warning', 'type': 'None'}, 'label': {'class': 'warning', 'type': 'Yet to implement'}}
    if request.method == 'POST':
        if request.POST.get('action') == 'send_image':
            data_from_post = request.POST.get('image')
            request.session['image'] = data_from_post[22:]

        if request.POST.get('action') == 'post_image':
            data_from_post = request.session['image']
            model = "ex3_modelx"  # Dit moet opgevraagd worden  #For make model
            shape = request.session['values']['shape'] #For make model settings if ever needed
            color = request.session['values']['color'] #For make model settings if ever needed
            identifier = request.session['identifier']  # Make session to select model
            response_color = json.loads(send_color_request(data_from_post, identifier))
            response_shape = json.loads(send_shape_request(data_from_post, identifier))
            print(response_shape, response_color)

            if response_shape['type'] == "error":
                print(response_shape['message'])
                response['shape']['type'] = "Error"
                response['shape']['class'] = "negative"
            elif response_shape['message'] == True:
                response['shape']['class'] = "positive"
                response['shape']['type'] = "Accepted"
            elif response_shape['message'] == False:
                response['shape']['class'] = "negative"
                response['shape']['type'] = "Denied"

            if response_color['type'] == "error":
                print(response_shape['message']) #TODO weergeven op pagina
                response['color']['type'] = "Error"
                response['color']['class'] = "negative"
            elif response_color['message'] == True:
                response['color']['class'] = "positive"
                response['color']['type'] = "Accepted"
            elif response_color['message'] == False:
                response['color']['class'] = "negative"
                response['color']['type'] = "Denied"

        if request.POST.get('action') == 'new_model':
            values = check_for_session(request)
            print(values)
            # Set vars
            modelimg = request.session['image']
            model_name = request.POST.get('model_name')
            # Create models
            print('send_shapemodel_request...')
            response_shapemodel_request = send_shapemodel_request(modelimg, model_name + '_shape', values['shape'])
            response_shapemodel_request = json.loads(response_shapemodel_request)
            if response_shapemodel_request['type'] != "error":
                contour = response_shapemodel_request['message']['contour']
            else:
                contour = ''
            print('send_colormodel_request...')
            response_colormodel_request = send_colormodel_request(modelimg, model_name + '_color', values['color'], contour)
            print("Response from shape: ", response_shapemodel_request) #TODO Weergeven op pagina
            print("Response from color: ", response_colormodel_request) #TODO Weergeven op pagina

        if request.POST.get('action') == 'remove_model':    #Remove model TODO geeft nog een error dat identifier niet bestaat
            identifier = request.POST.get('identifier')
            delmodel = del_model(identifier)
            print(delmodel)
        if request.POST.get('action') == 'change_model': #Change model to send images to
            request.session['identifier'] = request.POST.get('identifier')

    template = loader.get_template('app/index.html')
    context = {'models': models, 'response': response}

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

    template = loader.get_template('app/settings.html')
    context = {'form': values}
    return HttpResponse(template.render(context['form']))

def information(request):
    template = loader.get_template('app/information.html')
    context = {}
    return HttpResponse(template.render(context))