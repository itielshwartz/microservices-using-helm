FROM python:3.7-slim

WORKDIR /usr/src/index

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]