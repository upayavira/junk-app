from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
  a = int(request.args["a"])
  b = int(request.args["b"])
  c = a+b

  return '{"c":%s}' % c

app.run("0.0.0.0", 8080, debug=True)

