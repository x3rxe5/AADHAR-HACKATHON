# AADHAR HACKATHON

Table of contents
=================

<!--ts-->
    * [Installation](#installation)
        * [standard way][#standardway]  
        * [using docker][#usingdocker]   
<!--te-->


Installation
============


standard way
------------

```bash
# install the requirements module
pip install -r requirements.txt

# for running scripts
python3 server.py

#  --- OR --- 
# from the terminal you can type command
uvicorn src.main:app --reload
```

using docker
------------

> :warning: **Check the sudo privledge before running docker command**:
>[!WARNING]
>Check the sudo priviledge before running docker command
```bash


# build docker file 
docker-compose build

# run the container 
docker-compose up -d

```
