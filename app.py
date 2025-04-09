from flask import Flask, render_template, request
from chatbot.retrieval_generation import generation
from chatbot.data_ingestion import data_ingestion
from flask_cors import CORS
import logging


# vstore = data_ingestion("done")
# chain = generation(vstore)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    vstore = data_ingestion("done")
    logging.info("Vector store initialized successfully.")
    chain = generation(vstore)
    logging.info("Generation chain initialized successfully.")
except Exception as e:
    logging.error(f"Error during initialization: {e}")
    # Potentially exit the application if initialization fails
    # import sys
    # sys.exit(1)


app = Flask(__name__, static_folder='static')
CORS(app)

# @app.route("/")
# def index():
#     return "Hello from the backend!"
@app.route("/")
def index():
    return render_template("index.html")



@app.route("/get", methods=["POST", "GET"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        input = msg
        print(f"Received message: {input}")  # Add this line

        try:
            result = chain.invoke(
                {"input": input},
                config={"configurable": {"session_id": "dhruv"}},
            )["answer"]
            print(f"Chatbot result: {result}")  # Add this line
            return str(result)
        except Exception as e:
            print(f"Error during chatbot processing: {e}")
            return "Error processing your request." # Return an error to the frontend
    return "Please send a POST request with a message."

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=10000, debug= False)