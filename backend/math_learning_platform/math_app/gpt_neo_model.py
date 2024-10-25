from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)