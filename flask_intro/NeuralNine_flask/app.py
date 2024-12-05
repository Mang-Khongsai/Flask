from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!!"

# /hello should necessarily not be the same as the function name
@app.route('/hello')
def hello():
    return "<h1>Hello World again</h1>"

if __name__ == "__main__":
    # 5555 is a local host , we can write any value
    app.run(host='0.0.0.0',port=7777, debug=True)   
    
    # its the same as code below that is without host value
    #app.run(host='0.0.0.0', debug=True)
    #app.run(debug=True)  