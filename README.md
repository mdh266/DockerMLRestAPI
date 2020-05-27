# Dockerized Machine Learning Rest API
---------------------

Example of turning an [XGBoost](http://xgboost.readthedocs.io/) model (built [here]https://github.com/mdh266/NYCBuildingEnergyUse)) using [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Docker](https://www.docker.com/) and [Google Cloud Run:](hhttps://cloud.google.com/run).

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


## Deploying to Google Cloud Run:
------------------------
Build image on Google Cloud

	cd app

	gcloud builds submit --tag gcr.io/<project-id>/mlapp

Deploy to Google Engine App:

	gcloud run deploy --image gcr.io/<project-id>/mlapp --platform managed


