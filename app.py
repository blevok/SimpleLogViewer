from flask import Flask, render_template, redirect, request, Response, url_for
from functools import wraps
import os
from datetime import datetime as dt

application = Flask(__name__)
application.jinja_env.auto_reload = True
application.config["TEMPLATES_AUTO_RELOAD"] = True

global lines
lines = 26

# https://stackoverflow.com/questions/29725217/password-protect-one-webpage-in-flask-app
def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'username' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@application.route("/")
@requires_auth
def index():
    return render_template("index.html")

def get_time():
    return dt.now()

@application.route("/", methods =["GET", "POST"]) 
def update_logs():
    if request.method == 'POST':
        if request.form['submit_button'] == '25 Lines':
            global lines 
            lines = 26
            set_lines(26)
            return render_template('index.html')
        elif request.form['submit_button'] == '50 Lines':
            global lines
            lines = 51
            set_lines(51)
            return render_template('index.html')
        elif request.form['submit_button'] == '100 Lines':
            global lines
            lines = 101
            set_lines(101)
            return render_template('index.html')
        elif request.form['submit_button'] == '250 Lines':
            global lines
            lines = 251
            set_lines(251)
            return render_template('index.html')
        elif request.form['submit_button'] == '500 Lines':
            global lines
            lines = 501
            set_lines(501)
            return render_template('index.html')
        elif request.form['submit_button'] == '1000 Lines':
            global lines
            lines = 1001
            set_lines(1001)
            return render_template('index.html')
        else:
            pass

def set_lines(number):
    global lines
    lines = number
    
def number_of_lines():
    actual_lines = lines - 1
    return actual_lines

def get_log_lines():
    last_lines = get_last_n_lines("/path/to/log/file.log", lines)
    return last_lines

# https://thispointer.com/python-get-last-n-lines-of-a-text-file-like-tail-command/
def get_last_n_lines(file_name, N):
    # Create an empty list to keep the track of last N lines
    list_of_lines = []
    # Open file for reading in binary mode
    with open(file_name, 'rb') as read_obj:
        # Move the cursor to the end of the file
        read_obj.seek(0, os.SEEK_END)
        # Create a buffer to keep the last read line
        buffer = bytearray()
        # Get the current position of pointer i.e eof
        pointer_location = read_obj.tell()
        # Loop till pointer reaches the top of the file
        while pointer_location >= 0:
            # Move the file pointer to the location pointed by pointer_location
            read_obj.seek(pointer_location)
            # Shift pointer location by -1
            pointer_location = pointer_location -1
            # read that byte / character
            new_byte = read_obj.read(1)
            # If the read byte is new line character then it means one line is read
            if new_byte == b'\n':
                # Save the line in list of lines
                list_of_lines.append(buffer.decode()[::-1])
                # If the size of list reaches N, then return the reversed list
                if len(list_of_lines) == N:
                    return list(reversed(list_of_lines))
                # Reinitialize the byte array to save next line
                buffer = bytearray()
            else:
                # If last read character is not eol then add it in buffer
                buffer.extend(new_byte)
        # As file is read completely, if there is still data in buffer, then its first line.
        if len(buffer) > 0:
            list_of_lines.append(buffer.decode()[::-1])
    # return the reversed list
    return list(reversed(list_of_lines))

application.jinja_env.globals.update(
    get_log_lines=get_log_lines,
    get_time=get_time,
    number_of_lines=number_of_lines,
)

if __name__ == "__main__":
    application.run(host='0.0.0.0')