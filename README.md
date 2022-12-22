# DataQuality
This project is running a data pipeline to intake a Pandas DataFrame, utilize Captial One's DataProfiler to get information on the dataframe, and then save the results into a MongoDB. The data pipeline itself will run in one Docker Container and the MongoDB will run in another container. 

#Getting started

Run the following docker command to build the image from the dockerfile

docker build -t dev_quality .



then run the following docker command to start the container 
docker container run -it dev_dataquality /bin/bash
