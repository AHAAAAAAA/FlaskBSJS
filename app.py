#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about') #About page
def about():
	# Passing on data to About page
	data = {"name":"Ahmed", "age":22, "email":"Ahmed.Almutawa@colorado.edu",
			"twitter":"waishda", "github":"AHAAAAAAA", "summary":"Blah, blah, blah."}
	ppimg = "https://pbs.twimg.com/profile_images/681195421629296641/Ioaz3eKA_400x400.jpg"
	return render_template('about.html', data=data, ppimg=ppimg)

@app.route('/_submit') #AJAX endpoint
def submit():
	a = request.args.get('n1', 0, type=int)
	b = request.args.get('n2', 0, type=int)
	print(a, b)
	return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(debug=True)
