import time
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(404)
def not_found(e):
    return {'error': 'Not Found'}, 404

@app.route('/api/time')
@cross_origin()
def get_current_time():
    return {'time': time.time()}

@app.route('/')
@cross_origin()
def get_root():
    return {'status': 'ok'}
