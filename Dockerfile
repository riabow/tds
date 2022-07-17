FROM python:3.9
WORKDIR tds
COPY HelloDjango HelloDjango
COPY static static
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8001

CMD ["python", "HelloDjango/manage.py", "runserver", "0.0.0.0:8001"]

