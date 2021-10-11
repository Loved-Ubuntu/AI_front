from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
import json
#from Frond_end_django.comparisonHttp import send_image_color, send_image_shape
from Frond_end_django.comparisonHttp import *

@csrf_exempt
def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    if request.method == 'POST':
        data_from_post = json.load(request)['image']

        # Load model image
        modelimg = _loadimg(r'D:\Desktop\Project BD02\Back ENd\ex3_model.jpg')
        # Load bad shape image (distorted)
        badshapeimg = _loadimg(r"D:\Desktop\Project BD02\Back ENd\ex3_distort.jpg")
        # Load bad color image (discoloured)
        badcolorimg = _loadimg(r"D:\Desktop\Project BD02\Back ENd\ex3_color.jpg")

        # Create models
        print('send_shapemodel_request...')
        response_shapemodel_request = send_shapemodel_request(modelimg, 'ex3_model_shape')
        print('send_colormodel_request...')
        response_colormodel_request = send_colormodel_request(modelimg, 'ex3_model_color')
        # Send shape requests, one bad one good
        response_shape_request_bad = send_shape_request(badshapeimg, 'ex3_model_shape')
        print('send_shape_request_bad...')
        response_shape_request_good = send_shape_request(modelimg, 'ex3_model_shape')
        print('send_shape_request_good...')
        # Send color requests, one bad one good
        response_color_request_bad = send_color_request(badcolorimg, 'ex3_model_color')
        print('send_color_request_bad...')
        response_color_request_good = send_color_request(modelimg, 'ex3_model_color')
        print('send_color_request_good...')

        print("\nShape Model Request response:\t\t", response_shapemodel_request[:100]) #Remove this tag, and use the function to show a visual index
        print("\nColor Model Request response:\t\t", response_colormodel_request[:100]) #Remove this tag, and use the function to show a visual index
        print("\nShape Comparison Request response (Malformed):\t\t", response_shape_request_bad) #Remove this tag, and use the function to show a visual index
        print("\nShape Comparison Request response (Good):\t\t", response_shape_request_good) #Remove this tag, and use the function to show a visual index
        print("\nColor Comparison Request response (Discoloured):\t", response_color_request_bad) #Remove this tag, and use the function to show a visual index
        print("\nColor Comparison Request response (Good):\t\t", response_color_request_good) #Remove this tag, and use the function to show a visual index
    
        print('\n\tModels GET/DEL')
        models = get_models()[:200]
        print(f'\nAll models: {models}')
        delmodel = del_model('ex3_model_shape')
        print(f'\nDel Model ex3_model_shape: {delmodel}')
        getmodel = get_model('ex3_model_shape')[:100]
        print(f'Get Model ex3_model_shape: {getmodel}')
        models = get_models()[:200]
        print(f'\nAll models: {models}')


    return HttpResponse(template.render(context, request))

import base64
def _loadimg(path):
    with open(path, "rb") as imageFile:  # absolute path
        image_encoded = str(base64.b64encode(imageFile.read()), encoding='utf-8')
    return image_encoded