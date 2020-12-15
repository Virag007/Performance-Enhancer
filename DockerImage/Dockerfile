FROM python:3
WORKDIR /PEtrack
ADD requirements.txt ./
RUN pip install --no-cache -r requirements.txt
ADD PEtrack.py ./
CMD [ "python", "./PEtrack.py" ]