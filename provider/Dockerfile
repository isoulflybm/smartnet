# Use the official Python runtime image
FROM python:3.10.12
 
# Create the app directory
RUN mkdir /usr/app
 
# Set the working directory inside the container
WORKDIR /usr/app
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /usr/app/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
COPY . /usr/app/
 
# Expose the Django port
#EXPOSE 8000
 
# Run Django’s development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["daphne", "-b 0.0.0.0", "-p 8000", "provider.asgi:application"]

ENTRYPOINT ["/usr/app/entrypoint.sh"]