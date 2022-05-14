from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)
app.config['SECRET_KEY'] ='*m)y@12s#4e3@c$ret'


@app.route('/screen2', methods = ['GET','POST'])
def screen2():
    if request.method=='GET':
        return render_template('screen2.html')

@app.route('/screen1', methods = ['GET','POST'])
def screen1():
    if request.method=='GET':
        return render_template('screen1.html')

@app.route('/screen1_data', methods=['GET','POST'])
def screen1_data():
    if request.method=='POST':
        return render_template('screen1.html')
if __name__ == '__main__':
    app.run(debug=True, port =8080)