FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# set permition
RUN chmod 777 app.py

# Install dependencies
RUN pip install --user -r requirements.txt

# Expose port 
ENV PORT 8080

# Run the application:
CMD ["python", "app.py"]
