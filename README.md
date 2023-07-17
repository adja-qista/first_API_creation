# first_API_creation

### 1.packaging the code into an image
Open a terminal and cd to the directory that contains the Dockerfile. 
Then execute the following command: docker build . -t adja_api.

### 2.Running the image
docker run -it adja_api python -m uvicorn tuto:app --reload

### 3. Pushing to Docker Hub
First we’ll need to create an account: go to https://hub.docker.com to sign up. Then we need to create a repository; this is a place where your image will go. I’ve named mine medium_cmd_app.

The next step is to open a terminal, log in to Docker Hub and push (upload) your image. Here’s how to do it:

Open a terminal
CD to your project directory
docker login → enter your credentials
Build the image again but with the following tag:
docker build . -t [your_dockerhub_username]/[your_respo_name]
5. docker push [your_dockerhub_username]/[your_respo_name]
