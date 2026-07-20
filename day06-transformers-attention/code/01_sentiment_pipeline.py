"""
Day 6 - Part 1: Sentiment Analysis using a pretrained Transformer pipeline
Uses Hugging Face's pipeline() - the simplest way to run inference
with a pretrained model (DistilBERT fine-tuned for sentiment).
"""
from transformers import pipeline


def execute_pipeline_inference():
    """
    Initializes a text classification pipeline using
    a pre-trained DistilBERT model.
    """
    sentiment_analyzer = pipeline(
        task="sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1  # Use CPU (0 for GPU)
    )

    evaluation_texts = [
        "The instructional presentation was incredibly clear and offered profound, intuitive explanations.",
        "The network architecture is painfully slow, poorly optimized, and completely lacks clear documentation."
    ]

    inference_outputs = sentiment_analyzer(evaluation_texts)

    for text, output in zip(evaluation_texts, inference_outputs):
        print(f"Observed Text: '{text}'")
        print(f"Calculated Label: {output['label']} | Confidence Score: {output['score']:.4f}\n")


if __name__ == "__main__":
    execute_pipeline_inference()