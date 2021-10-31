# AADHAR HACKATHON
# Team No: 5adExgImzN

<br />
<hr />

Table of contents
=================


<!--ts-->  
   * [Installation](#installation)
      * [standard way](#standardway)
      * [using docker](#using-docker)
   * [API Refernce](#apireference)      
   * [Snap Shots](#snapshot)   
      * [Docker compose](#dockercompose)      
      * [Development](#development)      
      * [Request body](#requestbody)      
      * [Response Body example no. #1](#responsebodyExample1)      
      * [Response Body example no. #2](#responsebodyExample2)   
   * [Example Video](#exampleVideo)      
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
## for production please change the file server.py and register localhost and port name in it

```bash
if __name__ == "__main__":
    uvicorn.run(app,host=<hostname>,port=<portnumber>,log_level="info")
```

using docker
------------

> :warning: **Check the sudo privilege before running docker command**:

```bash


# build docker file 
docker-compose build

# run the container 
docker-compose up -d

```

API Refernce
============

```bash
   # please prefer the language code from /src/logic/language_dict.py
   [ROUTE EXAMPLE] : http://localhost:8000/api/v1/address/?lang=[language name]
   # it is post request 
   [POST]          : http://localhost:8000/api/v1/address/?lang=gu   
```


Snap Shots
==========

```Docker compose```
----------------------
![Docker Compose](./images/docker-compose.png?raw=true "Docker Compose")

```Development```
------------------
![Development](./images/development.png?raw=true "Development")

```Request body```
-------------------
![Request Body](./images/Request_Body.png?raw=true "Request Body")

```Response Body example no. #1```
-----------------------------------
![Response Body #1](./images/response_body_11.png?raw=true "Response Body #1")

```Response Body example no. #2```
----------------------------------
![Response Body #2](./images/response_body_2.png?raw=true "Response Body #2")


Example Video
=============