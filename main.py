from flask import Flask, request

from search import search
from sorter import sorter
import vaex
import os

app = Flask(__name__)

dv = vaex.open(r'db/road-fr.hdf5')

dv_zone_fr = {}

def initZoneForSearch(v, c):
    directory = c
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        key = filename.split(".")
        if(filename[len(filename) - 1] == "5"):
            currentDv = vaex.open(f)
            v[key[0]] = currentDv

initZoneForSearch(dv_zone_fr, 'fr')

@app.route('/sorter', methods=['GET'])
def api_sorter():
    return sorter()

@app.route('/search', methods=['GET'])
def api_search():
    if(request.args['country'] == "fr"):
        return search(dv_zone_fr, dv)

@app.route('/', methods=['GET'])
def say_hello():
    return "Goliv api v.2.0.1 by Manhamprod"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
