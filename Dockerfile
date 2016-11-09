FROM python:2.7-onbuild

RUN sudo pip install -U nltk && python -m nltk.downloader -d /usr/src/app/nltk_data all

CMD [ "python", "./server.py" ]