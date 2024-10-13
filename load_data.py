from datasets import load_dataset
from haystack import Document


dataset = load_dataset("Ashwagandna/DSC", split="train")


docs = [Document(content=doc["content"]) for doc in dataset]

