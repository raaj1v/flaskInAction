from  flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
  return "Hello World"

if __name__ == "__main__":
  print("inside the if now")
  app.run(host="0.0.0.0", debug=True)