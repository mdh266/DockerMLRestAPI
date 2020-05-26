FROM continuumio/miniconda3:4.7.10

# set up file system
RUN mkdir ds
RUN mkdir ds/model
WORKDIR /ds

# copy the files over
COPY main.py /ds
COPY model/xgbmodel.joblib /ds/model
COPY requirements.txt /ds/

RUN pip install -r /ds/requirements.txt

# run the app
# ENTRYPOINT ["gunicorn"]
EXPOSE 8080
CMD ["gunicorn", "-w","2", "-b","0.0.0.0:8080","main:app"]
