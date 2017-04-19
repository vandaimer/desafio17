from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')
