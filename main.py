from flask import Flask, request

from search import getPlace
from sorter import sorter
import vaex

app = Flask(__name__)

dv = vaex.open(r'db/road.csv.hdf5')

@app.route('/sorter', methods=['GET'])
def api_sorter():
    return sorter()

@app.route('/search', methods=['GET'])
def api_search():
    search = getPlace(request.args['city'], None, request.args['search'].upper())
    return search

@app.route('/', methods=['GET'])
def say_hello():
    return "Goliv api v.1.1.0 by Manhamprod"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
