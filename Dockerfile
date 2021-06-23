FROM python:3.7


WORKDIR /app
ADD . /app


# Install dependencies
RUN pip install -r requirements.txt

RUN chmod -R 777 /app

# Run the application:
CMD ["python", "app.py"]
