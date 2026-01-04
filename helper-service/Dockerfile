FROM python:3

WORKDIR /api

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

EXPOSE 9000

CMD [ "fastapi", "run", "main.py", "--port", "9000" ]