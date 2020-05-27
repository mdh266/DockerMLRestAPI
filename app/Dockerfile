FROM continuumio/miniconda3:4.7.10

# install dependencies first
RUN pip install flask==1.0.2\
                joblib==0.13.2\
                pandas==1.0.1\
                xgboost==1.0.2\
                gunicorn==19.9.0


# set up file system
RUN mkdir ds
RUN mkdir ds/model
WORKDIR /ds

# copy the files over
COPY main.py /ds
COPY model/xgbmodel.joblib /ds/model

CMD ["gunicorn", "-w","2", "-b","0.0.0.0:8080","main:app"]
