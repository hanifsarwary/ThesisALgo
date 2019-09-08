FROM python:3

RUN pip install numpy

ADD algo.py /

ADD GUI.py /

ADD Node.py /

ADD input.txt /



CMD ["python", "./algo.py"]