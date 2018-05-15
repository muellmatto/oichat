#!/usr/bin/env python3
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bier!!!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('oimessage', namespace='/test')
def oi_message(message):
    emit('oi response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('oi response', {'data': 'Connected'})

#@socketio.on('disconnect', namespace='/test')
#def test_disconnect():
#    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, port=62004)
