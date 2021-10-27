# AADHAR HACKATHON

Table of contents
=================

<!--ts-->
   * [Installation](#installation)
      * [standard way][#standardway]  
      * [using docker][#docker]   
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

```bash

> :warning: **Check the sudo privledge before running docker command**:

# build docker file 
docker-compose build

# run the container 
docker-compose up -d

```
