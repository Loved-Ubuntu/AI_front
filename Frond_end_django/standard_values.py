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