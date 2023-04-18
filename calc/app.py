# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# a = request.args['int:a']
# b = request.args['int:b']



@app.route('/add')
def do_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))   
    return f'{add(a,b)}'


@app.route('/sub')
def do_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))   
    return f'{sub(a,b)}'

@app.route('/mult')
def do_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))   
    return f'{mult(a,b)}'

@app.route('/div')
def do_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))   
    return f'{div(a,b)}'

OPERATORS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
    }


@app.route('/math/<operator>')
def do_math(operator):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))  
    op = OPERATORS[operator]
    return f'{op(a,b)}'
