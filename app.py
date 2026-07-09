from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
  return("<h1>Python web application hosted successfully</h1>")
  if__name__=="__main__":
  app.run()
  
