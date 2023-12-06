FROM python:3.10

ENV PYTHONNUNBUFFERED=1

WORKDIR /code/

COPY requirements.txt .

RUN pip3 install -r  requirements.txt

COPY . .


RUN python manage.py migrate


EXPOSE 8000


CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]



#__________________ Dockerfile Documentation_____________________________#
# Base Image:

# FROM python:3.10
# Description: Uses Python 3.10 as the base image for the Docker container.
# Environment Variable:

# ENV PYTHONUNBUFFERED=1
# Description: Sets unbuffered mode for Python, improving debugging.
# Working Directory:

# WORKDIR /code/
# Description: Sets the working directory to /code/ inside the container.
# Copying Requirements:

# COPY requirements.txt .
# Description: Copies Python dependencies list to the container.
# Installing Dependencies:

# RUN pip3 install -r requirements.txt
# Description: Installs dependencies specified in requirements.txt.
# Copying Code:

# COPY . .
# Description: Copies the application code to the container.
# Running Migrations:

# RUN python manage.py migrate
# Description: Applies Django database migrations.
# Expose Port:

# EXPOSE 8000
# Description: Informs Docker that the application uses port 8000.
# Default Command:

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# Description: Sets the default command to run the Django development server


# ________________________________________________________________________________

# Build Image:

# docker build -t image_name .
# docker run -p 8000:8000 your_image_name or -it image id 


















































































































  

















