# SimpleLogViewer

This is a very simple Flask app that outputs the last n lines of a log file to a web page.
By default you can choose the last 25, 50, 100, 250, 500, or 1000 lines, but you can easily add other options. Click any of the buttons to update the log or change the length.

There is a basic authentication function to restrict access.


### Setup

1. Create a folder for the log viewer\
```mkdir /home/user/logviewer```

2. CD to the new folder and clone the repo\
```cd /home/user/logviewer```\
```git clone https://github.com/blevok/SimpleLogViewer.git```

3. Create a virtual environment\
```python3 -m venv logviewerenv```

4. Activate the virtual environment\
```source logviewerenv/bin/activate```

5. Install wheel, flask, and gunicorn in the virtual environment\
```pip install wheel```\
```pip install gunicorn flask```

6. Edit app.py
- Line 18 - set a username and password
- Line 89 - set the path to the log file you want to see on the web page


### Usage

1. Run the app with gunicorn. Use a different port if 5000 is already in use\
```gunicorn --bind 0.0.0.0:5000 wsgi```

2. Go to your-server-ip:5000 in a browser and you should be prompted to login, and then you'll see the log file

3. When you're finished, press Ctrl+C to stop the app

4. Deactivate the virtual environment\
```deactivate```

If you want to leave the app running after you close the terminal, you can run it in screen.


### Next steps

You can setup nginx or other web server to proxy requests and use a domain name.

You can install an SSL certificate to secure the log viewer.

You can add a systemd service file to run the app when the system starts.

### Screenshot

![SimpleLogViewer](https://raw.githubusercontent.com/blevok/SimpleLogViewer/master/simplelogviewer.png)