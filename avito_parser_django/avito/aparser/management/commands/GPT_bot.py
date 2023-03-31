#pip install transformers
#pip install openai
#python --version >= 3.11

# from transformers import AutoTokenizer, AutoModelWithLMHead
# import openai
#
# tokenizer = AutoTokenizer.from_pretrained("gpt2")
# model = AutoModelWithLMHead.from_pretrained("gpt2")
# prompt = "There are five"
# input_ids = tokenizer.encode(prompt, return_tensors='pt')
# outputs = model.generate(input_ids, max_length=50, do_sample=True)
# generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print(generated_text)

import os
import openai
key_api = 'x7e9jy6zp8dgfh3w2q1k5m4c0b'
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = key_api

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)