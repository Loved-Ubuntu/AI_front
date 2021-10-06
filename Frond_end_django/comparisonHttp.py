def send_image_shape(image_encoded):
	import requests
	import json
	import socket
	# Hier uitzoeken wat het IP van de Back-end service zal zijn in het Docker netwerk
	# Normaal kan je dat statisch krijgen in het Netwerk
	# De gekozen port moet ook in de Back-end en Front-end (client side) consistent zijn
	url = f'http://{socket.gethostbyname(socket.gethostname())}:30303/'

	jsonRequest = {
		'type': 'shapeModel',
		'identifier': 'ex3_model_shape',
		'inputImage': image_encoded,
		'imageOperations': [
			{
				'operation': 'scale',
				'arg': {'scale': 0.1}
			},
			{
				'operation': 'blur',
				'arg': {}
			},
			{
				'operation': 'edges',
				'arg': {'lower': 20, 'upper': 300}
			},
			{
				'operation': 'grayscale',
				'arg': {}
			},
			{
				'operation': 'threshold',
				'arg': {'T': 128, 'fill': 255}
			},
		],
	}

	jsonRequest = json.dumps(jsonRequest)  # Encoden naar json-string
	response = requests.post(url, data=jsonRequest)  # POST Request naar server met alle json data
	print(json.loads(response.text))  # Print de response text (json string)
	return response

def send_image_color(image_encoded):
    import requests
    import json
    import socket

    # Hier uitzoeken wat het IP van de Back-end service zal zijn in het Docker netwerk
    # Normaal kan je dat statisch krijgen in het Netwerk
    # De gekozen port moet ook in de Back-end en Front-end (client side) consistent zijn
    url = f'http://{socket.gethostbyname(socket.gethostname())}:30303/'

    jsonRequest = {
        'type': 'color',
        'inputImage': image_encoded,
        'model': 'ex3_model_color',
        'cutoff': 0.1,
    }

    jsonRequest = json.dumps(jsonRequest)  # Encoden naar json-string
    response = requests.post(url, data=jsonRequest)  # POST Request naar server met alle json data

    return response