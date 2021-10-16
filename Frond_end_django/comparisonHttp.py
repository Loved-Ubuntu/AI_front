import requests
import json

url = f'http://localhost:30303/'


def send_shapemodel_request(image_encoded, identifier, shape):
    # Hier uitzoeken wat het IP van de Back-end service zal zijn in het Docker netwerk
    # Normaal kan je dat statisch krijgen in het Netwerk
    # De gekozen port moet ook in de Back-end en Front-end (client side) consistent zijn

    # image_encoded = image_encoded.split(',')[1]
    # print(type(image_encoded))
    # print(image_encoded[:50])

    jsonRequest = {
        'type': 'shapeModel',
        'identifier': identifier,
        'inputImage': image_encoded,
        'imageOperations': [
            {
                'operation': 'scale',
                'arg': {'scale': shape['scale']}
            },
            {
                'operation': 'blur',
                'arg': {}
            },
            {
                'operation': 'edges',
                'arg': {'lower': shape['edges']['lower'], 'upper': shape['edges']['upper']}
            },
            {
                'operation': 'grayscale',
                'arg': {}
            },
            {
                'operation': 'threshold',
                'arg': {'T': shape['threshold']['t'], 'fill': shape['threshold']['fill']}
            },
        ],
    }

    jsonRequest = json.dumps(jsonRequest)  # Encoden naar json-string
    response = requests.post(url, data=jsonRequest)  # POST Request naar server met alle json data
    # print(json.loads(response.text))  # Print de response text (json string)

    return response.text


def send_colormodel_request(image_encoded, identifier, color, contour):
    # Hier uitzoeken wat het IP van de Back-end service zal zijn in het Docker netwerk
    # Normaal kan je dat statisch krijgen in het Netwerk
    # De gekozen port moet ook in de Back-end en Front-end (client side) consistent zijn

    # image_encoded = image_encoded.split(',')[1]
    # print(type(image_encoded))
    # print(image_encoded[:50])

    jsonRequest = {
        'type': 'colorModel',
        'identifier': identifier,
        'inputImage': image_encoded,
        'contour': contour,
        'imageOperations': [
            {
                'operation': 'scale',
                'arg': {'scale': color['scale']}
            },
        ],
    }

    jsonRequest = json.dumps(jsonRequest)  # Encoden naar json-string
    response = requests.post(url, data=jsonRequest)  # POST Request naar server met alle json data
    # print(json.loads(response.text))  # Print de response text (json string)

    return response.text


def send_color_request(image_encoded, modelIdentifier):
    # Hier uitzoeken wat het IP van de Back-end service zal zijn in het Docker netwerk
    # Normaal kan je dat statisch krijgen in het Netwerk
    # De gekozen port moet ook in de Back-end en Front-end (client side) consistent zijn

    # image_encoded = image_encoded.split(',')[1]
    # print(type(image_encoded))
    # print(image_encoded[:50])

    jsonRequest = {
        'type': 'color',
        'inputImage': image_encoded,
        'model': modelIdentifier,
        'cutoff': 0.1,
    }

    jsonRequest = json.dumps(jsonRequest)  # Encoden naar json-string
    response = requests.post(url, data=jsonRequest)  # POST Request naar server met alle json data

    return response.text


def send_shape_request(image_encoded, modelIdentifier):
    # Hier uitzoeken wat het IP van de Back-end service zal zijn in het Docker netwerk
    # Normaal kan je dat statisch krijgen in het Netwerk
    # De gekozen port moet ook in de Back-end en Front-end (client side) consistent zijn

    # image_encoded = image_encoded.split(',')[1]
    # print(type(image_encoded))
    # print(image_encoded[:50])

    jsonRequest = {
        'type': 'shape',
        'inputImage': image_encoded,
        'model': modelIdentifier,
        'cutoff': 0.01,
    }

    jsonRequest = json.dumps(jsonRequest)  # Encoden naar json-string
    response = requests.post(url, data=jsonRequest)  # POST Request naar server met alle json data

    return response.text


def get_model(identifier):
    response = requests.get(f'{url}/models/{identifier}')  # GET Request naar server voor een model
    return response.text


def get_models():
    response = requests.get(f'{url}/models/')  # GET Request naar server voor alle models
    return response.text


def del_model(identifier):
    response = requests.delete(f'{url}/models/{identifier}')  # DELETE Request naar server voor een model
    return response.text