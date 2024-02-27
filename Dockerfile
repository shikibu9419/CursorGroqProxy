FROM python:3.9

RUN apt-get update && apt-get upgrade -y

EXPOSE 8000

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip uvicorn
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
