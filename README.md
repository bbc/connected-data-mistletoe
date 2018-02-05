# Google Container Engine Skeleton Service

Skeleton Google Container Engine (GKE) service. Implemented with the Python 2
[Flask](http://flask.pocoo.org/) microframework.

## Run Locally
1. Create a virtualenv, install dependencies:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
2. Run the service:
```
python app.py
```

3. Visit the application at http://localhost:5000.

## Building & Deployment

This app is provided as with a Dockerfile which is used to build a container.
This should then be pushed to a container registry and deployed either as a
manual process or using something such as build triggers and a continuous
delivery platform like [Spinnaker](https://www.spinnaker.io/).
