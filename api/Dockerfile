FROM python:3.9

WORKDIR /api

COPY . /api

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

CMD ["python3", "main.py"]