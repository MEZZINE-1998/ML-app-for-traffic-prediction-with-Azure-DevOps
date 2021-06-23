FROM python:3.7


WORKDIR /app
ADD . /app


# Install dependencies
RUN pip install -r requirements.txt

RUN chmod -R 777 /app
RUN chmod 777 /app/app.py

# Run the application:
CMD ["python", "app.py"]
