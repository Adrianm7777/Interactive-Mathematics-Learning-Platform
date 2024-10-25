from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_math_problem(prompt:str):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["inputs_ids"], max_length=100, do_sample = True, temperature= 0.7)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text