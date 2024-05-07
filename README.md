# nodejs-app
Running nodejs application which asks a person's basic details like name and email then store them into a mongoDB database in backend

# Instructions to build docker images:

Node-app:

> docker build nodeapp ./node-app/Dockerfile .

MongoDB:

> docker build ./mongodb/Dockerfile .

Then push the created images into docker-hub or any repository and then mention the image names into the deployment file of each app.

# Instructions to deploy apps into kuberntes:

MongoDB:

> cd mongodb
> kubectl apply -f mongodb-deployment.yaml

 1. Please add Mongo-DB kubernetes service endpoint in the "// Connect to MongoDB" section of app.json file for 
    application and DB connectivity. [you will get this after deploying mongoDB into kubernetes]

Node-app:

> cd node-app
> kubectl apply -f nodejs-deployment.yaml

# After deployment:

1. Get the IP address of the node-application service and try to access that from the browser

   > kubectl get svc -A | grep nodejs

Copy the External-IP address from the above command output and then hit it in the browser, then give your name and email as input and it will store it in the Mongodb in the backend.
