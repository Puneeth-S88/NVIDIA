"""
Day 6 - Part 3: Extracting Encoder Hidden State Embeddings
Pulls the transformer's internal representation of a sentence
(the "middle state") instead of a final classification label.
"""
import torch
from transformers import AutoTokenizer, AutoModel


def extract_hidden_state_embeddings(text_batch):
    """
    Extracts high-dimensional latent vectors directly from the final
    encoder layer of a pre-trained Transformer backbone.
    """
    model_name = "distilbert-base-uncased"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    inputs = tokenizer(
        text_batch,
        padding=True,
        truncation=True,
        return_tensors="pt"
    )

    model.eval()

    with torch.no_grad():
        model_outputs = model(**inputs)

    # Output shape: [Batch Size, Sequence Length, Hidden Dimension]
    last_hidden_states = model_outputs.last_hidden_state

    # Extract the first token embedding (CLS-equivalent for DistilBERT)
    sentence_level_embeddings = last_hidden_states[:, 0, :].numpy()

    print("Full Encoder Output Matrix Shape:", last_hidden_states.shape)
    print("Extracted Sentence Context Vector Shape:", sentence_level_embeddings.shape)

    return sentence_level_embeddings


if __name__ == "__main__":
    sample_corpus = [
        "Highly scalable context vectors.",
        "Extracting mathematical features."
    ]

    embeddings = extract_hidden_state_embeddings(sample_corpus)

    print("\nSentence Embeddings:")
    print(embeddings)