FROM python:3

RUN git clone https://github.com/um-computacion-tm/parcial-2021-11-03-marcosricciardi12.git

WORKDIR /parcial-2021-11-03-marcosricciardi12

CMD ["python3", "test_buscaminas.py"]
