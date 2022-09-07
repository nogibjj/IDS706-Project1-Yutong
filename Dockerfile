FROM python:3.9

RUN mkdir -p /project
WORKDIR /project

COPY ./requirements.txt /project/requirements.txt
COPY ./Makefile /project/Makefile
RUN make

COPY ./src /project/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]