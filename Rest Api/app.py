from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/multiply', methods=['POST','GET'])
def multiply()-> str:
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if isinstance(a,int)==False or isinstance(b,int)==False:
        print("not int value")
        raise ValueError()
    if a<0 or b<0:
        print("taked negative number")
        raise TypeError()
    c=0
    for i in range(b):
        c += a
    return str(c)
@app.route('/kto-krasava')
def main():
    return request.args.get("name")
if __name__=='main':
    app.run(debug=True)