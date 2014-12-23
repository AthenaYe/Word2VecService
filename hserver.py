#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from flask import Flask, request
import sys
import readvec
import numpy as np
import scipy.spatial.distance.cosine

reload(sys)
sys.setdefaultencoding('UTF-8')

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World!"

@app.route("/vector")
def wordvector():
    word = request.args.get('w', None)
    if word is None:
        return "BAD", 400
    vec = lex.get(word, None)
    if not word:
        return "BAD", 400
    return vec

@app.route("/wordsimi")
def wordsimi():
    word1 = request.args.get('w1', None)
    word2 = request.args.get('w2', None)
    if not word1 and not word2:
        return "BAD", 400
    vec1 = lex.get(word1, None)
    vec2 = lex.get(word2, None)
    if not vec1 or not vec2:
        return "BAD", 400
#    return u"{}:{}".format(word1, word2)
    return cosine(vec1, vec2)


lex = readvec('vec2.bin')
app.run(debug=True, host='0.0.0.0', port=8000)


# vim: ts=4 sw=4 sts=4 expandtab
