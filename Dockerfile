FROM python:3.9
WORKDIR tds
COPY HelloDjango HelloDjango
COPY static static
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8001

CMD ["python", "HelloDjango/manage.py", "runserver", "127.0.0.1:8001"]

