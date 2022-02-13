#import dependencies
from flask import Flask

#create flask app
app = Flask(__name__)

#create first route
@app.route('/')
def hello_world():
    return 'Hello world.'

#Run the above in the command line.
#<export FLASK_APP=app.py>
#<flask run>
#copy and paste local host (http after "running on..."
# in terminal).