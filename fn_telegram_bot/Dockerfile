FROM python:3.8

WORKDIR /home/fn_telegram_bot

RUN pip install aiogram
RUN pip install requests

# RUN pip install fastapi uvicorn

# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN pip install psycopg2
# RUN pip install websockets
# RUN pip install aiohttp[speedups]
# RUN pip install SQLAlchemy
# RUN pip install pydantic

RUN echo "America/New_York" > /etc/timezone
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime
RUN echo "America/New_York" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# COPY . .
