# Day 6: Transformers, Attention & Classification Metrics

## Topics covered
- Transformer architecture: self-attention vs RNN/LSTM sequential processing
- Encoder (understanding text) vs Decoder (generating text)
- Tokenization: input_ids, attention_mask, padding, truncation
- Extracting hidden-state embeddings from a pretrained encoder
- Transfer learning: frozen transformer + custom classifier head
- Manual TP/TN/FP/FN, Precision, Recall, F1-Score, Accuracy calculation

## What I did
1. Ran a sentiment-analysis pipeline using pretrained DistilBERT
   (`distilbert-base-uncased-finetuned-sst-2-english`).
2. Tokenized raw text into input_ids + attention_mask tensors.
3. Extracted the encoder's last_hidden_state and pulled the sentence-level
   (CLS-equivalent) embedding vector (768-dimensional).
4. Simulated the "frozen transformer + custom classifier head" pattern by
   training Logistic Regression on mock 768-dim embeddings.
5. Implemented Precision/Recall/F1/Accuracy from scratch in NumPy to
   understand the math behind sklearn's metrics.

## Key concepts
- RNN -> LSTM -> Transformer: each step solves the previous one's
  memory/parallelization limits. Transformers process the whole sequence
  at once via self-attention instead of word-by-word.
- Encoder-only models (BERT/DistilBERT) are best for understanding/
  classification. Decoder-only models (GPT) are best for generation.
- TP/FP/TN/FN definitions and how Precision (false-alarm control) vs
  Recall (catch-everything) trade off against each other.

## AI tool disclosure
Used Claude to explain transformer architecture, encoder vs decoder,
RNN/LSTM/Transformer differences, and the precision/recall/F1 math, and
to organize today's notebook code into structured script files for the
GitHub repo.