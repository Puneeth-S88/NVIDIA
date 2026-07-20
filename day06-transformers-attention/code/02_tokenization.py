"""
Day 6 - Part 2: Tokenization
Demonstrates converting raw text into numeric tensors (input_ids)
plus attention_mask, which tells the model which tokens are real
vs padding.
"""
import torch
from transformers import AutoTokenizer


def generate_tensor_inputs():
    """
    Demonstrates manual vocabulary mapping, text truncation,
    and padding rules using Hugging Face.
    """
    model_identifier = "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_identifier)

    sample_phrases = [
        "Transformers bypass sequential bottlenecks.",
        "Attention mechanisms preserve contextual semantics perfectly."
    ]

    encoded_inputs = tokenizer(
        sample_phrases,
        padding=True,
        truncation=True,
        max_length=16,
        return_tensors="pt"
    )

    print("Generated Input Token Indices (input_ids):")
    print(encoded_inputs["input_ids"])

    print("\nGenerated Parallel Attention Masks:")
    print(encoded_inputs["attention_mask"])

    return encoded_inputs


if __name__ == "__main__":
    tensor_batch = generate_tensor_inputs()