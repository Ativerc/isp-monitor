FROM python:3.8

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY isp_monitor isp_monitor

CMD ["uvicorn", "isp_monitor.api.main:app", "--host", "0.0.0.0", "--port", "80"]

