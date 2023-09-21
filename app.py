from flask import Flask, render_template, request, jsonify, redirect, url_for
from llama_cpp import Llama

app = Flask(__name__)

# Initialize the model
LLM = Llama(model_path="llama-2-7b-chat.Q8_0.gguf")

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/top_news')
def top_news():
    # Redirect to the external URL
    return redirect("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen")

@app.route('/text_summarization')
def text_summarization():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_input = data.get('user_input', '')

    # Generate a response from the model
    output = LLM(user_input)
    response = output["choices"][0]["text"]
    print(output)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
