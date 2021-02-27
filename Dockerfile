FROM python:3.8.5

WORKDIR /copypaste
COPY . .
RUN pip install -r requirements.txt
CMD python main.py
