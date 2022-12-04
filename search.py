from flask import request
import re
from spelling import speelingAbbre

def formatReg(search):

    formatedReg = search

    for sp in speelingAbbre:
        formatedReg = re.sub(sp[0], sp[1], formatedReg)

    # return search with regex or empty str
    return formatedReg


def getPlace(reg, dv):
    val = dv[dv.rue.str.contains(reg, regex=True)]
    
    gen = val.to_pandas_df(chunk_size=10)
    
    for i1, i2, chunk in gen:
        return chunk.values.tolist()
    
    return []
        
def getPlaceWithZone(reg, dv, city):

    currentDv = dv[city]
    
    val = currentDv[currentDv.rue.str.contains(reg, regex=True)]
    
    gen = val.to_pandas_df(chunk_size=10)
    
    for i1, i2, chunk in gen:
        return chunk.values.tolist()
    
    return []


def search(dv_city, dv_all):
    reg = formatReg(request.args['search'].upper())

    search = getPlaceWithZone(reg, dv_city, request.args['city'])

    if len(search) < 10:
        search = getPlace(reg, dv_all)
    

    return search
