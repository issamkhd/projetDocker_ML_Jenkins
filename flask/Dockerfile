FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

ADD requirements.txt /app

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app 
ADD . /app


# Install apache2 package
RUN apt-get update && apt-get install -y libsndfile-dev && apt-get install -y ffmpeg


EXPOSE 8080

# run the command to start uWSGI
CMD ["python3", "backend_service_main.py"]
