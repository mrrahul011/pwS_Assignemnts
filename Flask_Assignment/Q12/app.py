from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html', time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@socketio.on('update_time')
def update_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    emit('time_updated', current_time)

if __name__ == '__main__':
    socketio.run(app)
