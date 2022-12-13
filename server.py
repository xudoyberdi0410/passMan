from flask import Flask, request
import bcrypt

app = Flask(__name__)

@app.post("/reg")
def registration():
    username = request.json['username']
    if not username:
        response = app.response_class(
            status=400,
            response={'message': 'Please enter username'}
        )
        return response
    passowrd = request.json['password']
    if not passowrd:
        response = app.response_class(
            status=400,
            response={'message': 'Please enter password'}
        )
        return response

    hashed = bcrypt.hashpw(password=passowrd.encode('utf-8'), salt=bcrypt.gensalt())


    return {'message': [username, passowrd, str(hashed)]}

@app.post('/log')
def login():
    username = request.json['username']
    if not username:
        response = app.response_class(
            status=400,
            response={'message': 'Please enter username'}
        )
        return response
    passowrd = request.json['password']
    if not passowrd:
        response = app.response_class(
            status=400,
            response={'message': 'Please enter password'}
        )
        return response
    password = passowrd.encode('utf-8')
    byt_passowrd = b'$2b$12$LqDbBUeMngjfg1Wy6aYy1.kRUEHHrRkdmmAV/mX74jI8uW5HlHkYy'
    if not bcrypt.checkpw(password=password, hashed_password=byt_passowrd):
        response = app.response_class(
            status=400,
            response={'message': 'Password or username is wrong'}
        )
        return response
        

    return {'message': 'ok'}