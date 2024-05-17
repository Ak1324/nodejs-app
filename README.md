# flask-app
Running flask application which asks a person's basic details like name and email then store them into a mongoDB database in backend

# Instructions to build docker images:

flask-app:

> docker build flask ./flask/Dockerfile .

MongoDB:

> docker build ./mongodb/Dockerfile .

Then push the created images into docker-hub or any repository and then mention the image names into the deployment file of each app.

# Run the imagepull-secret.sh file after editing the file with your actual Dockerhub details where the above build images are stored

>> sh imagepull-secret.sh

# Instructions to deploy apps into kuberntes:

MongoDB:

> cd mongodb
> kubectl apply -f mongodb-deployment.yaml

NOTE: 1. Please add Mongo-DB kubernetes service endpoint in the "<your-mongodb-url>" section of app.json file for 
    application and DB connectivity. [you will get this after deploying mongoDB into kubernetes]

flask-app:

> cd node-app
> kubectl apply -f flask-deployment.yaml

# After deployment:

1. Get the IP address of the node-application service and try to access that from the browser

   > kubectl get svc -A | grep flask

Copy the External-IP address from the above command output and then hit it in the browser, then give your name and email as input and it will store it in the Mongodb in the backend.
