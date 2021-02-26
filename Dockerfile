FROM python:3.9.1

RUN mkdir src
COPY ./functions.py /src
COPY ./test_functions.py /src 
WORKDIR /src
RUN pip install numpy
RUN pip install pytest

CMD ["pytest"]
