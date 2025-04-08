from flask import Flask, render_template, request
from chatbot.retrieval_generation import generation
from chatbot.data_ingestion import data_ingestion
from flask_cors import CORS



vstore = data_ingestion("done")
chain = generation(vstore)


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/get", methods = ["POST", "GET"])
def chat():
   
   if request.method == "POST":
      msg = request.form["msg"]
      input = msg

      result = chain.invoke(
         {"input": input},
    config={
        "configurable": {"session_id": "dhruv"}
    },
)["answer"]

      return str(result)

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=10000, debug= True)