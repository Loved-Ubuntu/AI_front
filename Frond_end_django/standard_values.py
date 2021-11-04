def get_standard_values_shape():
    shape = {
        "scale": 0.1,
        "blur": "",
        "grayscale": "",
        "edges": {'lower': 20, 'upper': 300},
        "threshold": {'t': 128, 'fill': 255}
    }
    return(shape)

def get_standard_values_color():
    color = {
        "scale": 0.1
    }
    return (color)

def check_for_session(request):
    if 'values' in request.session:
        values = request.session['values']
    else:
        #Session.objects.all().delete()  # If session crash, run this
        shape = get_standard_values_shape()
        color = get_standard_values_color()
        request.session['values'] = {"shape": shape, "color": color}
        values = request.session['values']
        request.session['identifier'] = ''
        request.session['image'] = ''
    return values