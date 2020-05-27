# Dockerized Machine Learning Rest API
---------------------

A dockerized XGBoost model:

## Local Use
---------------

Build the image

	docker build -t mlapp app

Run the API locally:
	
	docker run -ip 8080:8080 mlapp

From Python:

	data = {'columns': ['Energy_Star', 'Site_EUI', 'NGI', 'EI', 'Residential'],
          'data': [[7744, 52.7, 45.9641802469, 10.1204555556, 1],
                   [9, 112.2, 25.9187489356, 29.7707095517, 1]]}


	import requests

	result = requests.post(url="http://0.0.0.0:8080/predict",
                         json=data)

	result.json() # [0.0031427741050720215, 0.007205158472061157]


## Deploying to Google App Engine:
------------------------
Build image 

	docker build -t mlapp app

Push to Google Container registry:

	docker tag mlapp gcr.io/<project-id>/mlapp:latest
	docker push gcr.io/<project-id>/mlapp:latest

Deploy to Google Engine App:

	docker app deploy --image-url=gcr.io/<project-id>/mlapp:latest
