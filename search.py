import re

from spelling import speelingAbbre


def formatReg(search):

    formatedReg = search

    for sp in speelingAbbre:
        formatedReg = re.sub(sp[0], sp[1], formatedReg)

    # return search with regex or empty str
    return formatedReg


def getPlace(zone, dv, search):
    
    reg = formatReg(search)
    
    val = dv[dv.rue.str.contains(reg, regex=True)]
    
    gen = val.to_pandas_df(chunk_size=10)

    count = 0
    result = []

    for i1, i2, chunk in gen:
        return chunk.values.tolist()
    
    return []
