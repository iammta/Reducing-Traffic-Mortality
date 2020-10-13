FROM continuumio/anaconda3:4.7.12
COPY . /usr/app1/
EXPOSE 5000
WORKDIR /usr/app1/
RUN pip install -r requirements.txt
