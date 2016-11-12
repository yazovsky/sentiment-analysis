FROM python:2.7-onbuild

RUN pip install -U nltk && yes n | python -m nltk.downloader -f -d /usr/src/app/nltk_data all

CMD [ "python", "./server.py" ]