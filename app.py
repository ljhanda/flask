from flask
import Flask

@app.route("/")
def home():
  return "Hello, Flask"

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, True)
