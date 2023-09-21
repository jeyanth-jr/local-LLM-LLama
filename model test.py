# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="llama-2-7b-chat.Q8_0.gguf")

# create a text prompt
prompt = "Q: Who is the first president of India? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])