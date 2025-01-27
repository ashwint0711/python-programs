# Overview 
This repo contains implementation of given programs in python,
Along with implementation of python reverse proxy server without using Flask.

## str-pattern solved using Regular expressions
I've solved the string pattern matching problem using regular expressions.

## No Flask server
Implemented a reverse proxy server without using `nginx` which listens on port 8000 and redirects requests based on endpoints specified in the url.
Along with `rev-proxy-handler.py` there are two more files : `no-flask-ping-pong.py` and `date-time.py`, these two are simple 
servers, used them to test reverse proxy server.

Run below command to run `rev-proxy-handler.py` :
> python3 rev-proxy-handler.py

Run below command to run `no-flask-ping-pong.py` :
> python3 no-flask-ping-pong.py

Run below command to run `date-time.py` :
> python3 date-time.py

### Test server
Fire command :
> curl localhost:8000/ping
or
> curl localhost:8000/time
