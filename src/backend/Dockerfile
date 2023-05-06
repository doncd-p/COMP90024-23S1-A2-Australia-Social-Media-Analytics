# syntax=docker/dockerfile:1

# set up the base python image
FROM python:3.11.3-slim-bullseye

# set the working directory
WORKDIR /backend

# duplicate the required library into the base image
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy all file into the image 
COPY . .

EXPOSE 8080

# start the program
CMD ["gunicorn" , "app:app", "-c", "gunicorn_config.py"]

# Build image:
# sudo docker image build -t backend .

# Run the container:
# sudo docker run -d --name backend --network di -p 0.0.0.0:8080:8080 backend:latest
