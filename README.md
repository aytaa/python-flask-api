# REST API example application

This is a simple Rest API that connects to Mysql.

The entire application is contained within the `app.py` file. 

## Install

    pip install

## Run the app

    python3 app.py
 

# REST API

The REST API to the example app is described below.

## Get list of Users

### Request

`GET /users/`

    curl -i -H 'Accept: application/json' http://localhost:5000/users/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {
        "name": "Jhone"
    }

## Create a new User

### Request

`POST /user/`

    curl -i -H 'Accept: application/json' -d 'name=Foo&status=new' http://localhost:5000/user

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {"id":1,"name":"Foo","status":"new"}

