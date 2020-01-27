# Deployment

## Students Will Be Able To
 - [x] Explain the purpose of deploying a machine learning model
 - [x] Review the purpose of [pickling a model](https://github.com/learn-co-students/cloud-services-and-deployment-seattle-ds-102819/blob/master/pickling.ipynb)
 - [x] Understand the basics of some popular deployment techniques
    - Full-stack web application
    - Cloud function
    - ML-specific deployment
 - [x] Start formulating a deployment plan for their business case

## Full-Stack Web Application Example: Flask
Flask means developing a full-stack web application.  It follows a model-view-controller (MVC) pattern and requires that you sometimes have to follow a "convention over configuration" pattern and put certain files in certain folders.

There are two main ways I recommend deploying a Flask app: [Heroku](https://devcenter.heroku.com/articles/deploying-python), or [AWS EC2](https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0).  The main difference is that Heroku uses "dynos", a type of container that gets fully re-created when the site is "woken up" based on certain config files it finds in a GitHub repo.  EC2 is more like a "real" computer, where you can SSH in and download things, log out, log back in, and those things will still be there.  EC2 gives you more configuration capabilities and more computational power, but also requires more setup than Heroku.

### Pricing
[Heroku free tier](https://www.heroku.com/pricing) allows one web app for free.  [AWS free tier](https://aws.amazon.com/ec2/pricing/) allows 750 hours of "micro" level server time per month.

### Pros
 - Free
 - Allows you to become more familiar with web development and have a shared vocabulary with software developers
 - You can generate data visualizations in Python (don't need to learn JavaScript, only HTML and CSS)
 - Supports a multi-step process with more than one user interaction
 - Single solution to get a live user interface you can link from your portfolio

### Cons
 - Learning curve for all of Flask can be steep
 - More systems administration work than a cloud function or ML model
 - Less realistic workflow (unless you are the only technical person on your team, you will probably not be expected to set up a web server)
 
### Documentation
 - [Flask app repo from 0624 cohort](https://github.com/learn-co-students/capstone-flask-app-template-seattle-ds-062419)
 - [Flask quickstart documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

## Cloud Function Example: Google Cloud Functions
Google Cloud Functions allow you to make a single function that can be called from a REST API interface.  The Python language versions are actually running on top of Flask, with as much boilerplate removed as possible.  So you still need to learn some Flask to be able to get everything working.

### Pricing
Up to 2 million free Cloud Function invocations per month.  [Free tier](https://cloud.google.com/free/) requires signing up with a credit card, but promises "No autocharge after free trial ends"

### Pros
 - Free
 - Makes a REST API interface, so you can demo with Postman or an HTML + JS web frontend (or collaborate with an SE alum to make a React frontend for you)
 - Only requires you to learn a little bit of Flask.  Nothing about production WSGI servers, or nginx, or ports.

### Cons
 - Not making a full-stack web app means you won't have the experience of making a full-stack web app
 - Sometimes there is a lot of "magic" happening with the implicit Flask app that makes it hard to debug.  Probably will not be compatible with TensorFlow, for example, because you don't have fine-grained control over the threading behavior.
 - If you want to deploy a web frontend, you'll need to find another tool.  (GitHub Pages works fine though!)
 - The platform is not designed specifically for ML models, so it might be annoyingly slow, or even so slow that it times out.
 - You can't generate any data visualizations in Python, they will have to be in JavaScript

### Documentation
1. [Writing cloud functions](https://cloud.google.com/functions/docs/writing/http)
2. [Deploying cloud functions](https://cloud.google.com/functions/docs/deploying/filesystem)
3. [Calling cloud functions](https://cloud.google.com/functions/docs/calling/http)

### Example
I have a working example of a Google Cloud function in the `google_cloud_function` folder.  You can call it right now by pasting this into your terminal:
```
curl -X POST -H "Content-type: application/json" -d '{"Alcohol": 12.82, "Malic acid": 3.37, "Ash": 2.3, "Alcalinity of ash": 19.5, "Magnesium": 88.0, "Total phenols": 1.48, "Flavanoids": 0.66, "Nonflavanoid phenols": 0.4, "Proanthocyanins": 0.97, "Color intensity": 10.26, "Hue": 0.72, "OD280/OD315 of diluted wines": 1.75, "Proline": 685.0}' https://us-central1-splendid-petal-256700.cloudfunctions.net/wine-predictor
```

## ML-Specific Deployment Example: Google Cloud AI Platform
Google Cloud AI Platform allows you to upload an exported model to the cloud, then make future requests to the cloud to make new predictions.  The primary use case seems to be people who are already very integrated into the Google Cloud ecosystem, since they encourage requesting predictions through their custom SDK in Python rather than through a standard REST API interface.

### Pricing
It looks like there is no free tier for this service.  [Pricing summary here.](https://cloud.google.com/ml-engine/docs/pricing)

### Pros
 - After installing their CLI, you only need to upload the model itself, no additional libraries or frameworks
 - If you need better performance, it's easy to pay more money to get that
 - This is a "real" tool that you might encounter on the job, and resembles most closely the type of systems administration you might need to do on the job
 - If you need to use TensorFlow, Google made both TensorFlow and this product, so they're likely to be the most compatible

### Cons
 - Not free
 - No clear, easy way to make an "open" REST API that can communicate with Postman or a simple web frontend
 - Requires versioning and other configuration work that is not necessary for our projects

### Documentation
1. [Exporting models for prediction](https://cloud.google.com/ml-engine/docs/exporting-for-prediction)
2. [Deploying models](https://cloud.google.com/ml-engine/docs/deploying-models)
3. [Getting online predictions in Python](https://cloud.google.com/ml-engine/docs/online-predict), [Getting online predictions via REST](https://cloud.google.com/ml-engine/docs/v1/predict-request)

## Other Examples
These particular tools are the ones that I happen to be most familiar with, but there are other options you might want to consider

**Full-Stack Web Development**
 - If you really want to dive into full-stack web development, [Django](https://www.djangoproject.com/start/) has more features than Flask
 - Besides Heroku and AWS EC2, you can also host websites with [Azure App Service](https://docs.microsoft.com/en-us/learn/modules/host-a-web-app-with-azure-app-service/index), [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps), [Google Cloud App Engine](https://cloud.google.com/python/getting-started/hello-world), [AWS Elatic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
 
**Cloud Functions**
 - [AWS Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html)
 - [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python)
 
**ML-Specific Deployment**
 - [IBM Watson Studio](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/pm_service_supported_frameworks.html)  (kind of a mixture between a cloud function and ML-specific deployment)
 - [AWS SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
 - [Azure Machine Learning](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py )
