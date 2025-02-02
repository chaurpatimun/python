from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1>DevOps is fun.</h1>'
 return '<h1>DevOps is tooooooooooooooooo fun.</h1>'
 return '<h1>Sanfebagar Mun.</h1>'
 return '<h1>Sanfebagar Mun.</h1>'
 return '<h1>Chaurpati r.m Mun.</h1>'
 return '<h1>Sanfebagar Mun.</h1>'
app.run(host='0.0.0.0',port=7000)
