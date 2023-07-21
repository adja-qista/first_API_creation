# first_API_creation

### 1.packaging the code into an image
docker build . -t adja_api 
docker run docker run -d -p 8000 adja_api  # to test on local


### 2. Pushing to Docker Hub
* docker tag adja_api adjamagatte16/first_fastapi1
* docker push [your_dockerhub_username]/[your_respo_name]: 
    docker push adjamagatte16/first_fastapi1

### 3.Running the image on my vm
* create a vm on gcp
* Allow tcp at port 8000 on the firewall for the vm
* docker run -d -p 8000:8000 adjamagatte16/first_fastapi1 
* see the result at the external @ of the vm with internal:external port: @/8000:8000
# AUTOMATE THE PROCESS