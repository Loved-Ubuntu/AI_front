def save_settings_shape(request, values):
    values['shape']['scale'] = request.POST.get('scale')
    values['shape']['blur'] = request.POST.get('blur')
    values['shape']['grayscale'] = request.POST.get('grayscale')
    values['shape']['edges']['lower'] = request.POST.get('edges_lower')
    values['shape']['edges']['upper'] = request.POST.get('edges_upper')
    values['shape']['threshold']['t'] = request.POST.get('threshold_t')
    values['shape']['threshold']['fill'] = request.POST.get('threshold_fill')
    return