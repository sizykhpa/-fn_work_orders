FROM python:3.8

WORKDIR /home/fn_fastapi

RUN pip install fastapi uvicorn

RUN pip install psycopg2
RUN pip install websockets
RUN pip install pip install SQLAlchemy
RUN pip install pydantic
RUN pip install requests

RUN echo "America/New_York" > /etc/timezone
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime
RUN echo "America/New_York" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]