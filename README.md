# SMS Spam Detector

A machine learning project that classifies SMS messages as spam or not spam using Python and Logistic Regression. Built in two versions to show progression from a basic approach to a smarter one.

## Version 1 — Bag of Words (spam_detector.py)

Converts each message into a list of 1s and 0s representing whether each vocabulary word appears in the message. Simple but limited — treats every word equally regardless of how common or rare it is.

## Version 2 — TF-IDF (spam_detector_v2.py)

Uses TF-IDF vectorization which gives each word a score based on how unique and important it is across all messages. Common words like "the" and "I" get low scores. Spam trigger words like "urgent" and "free" get high scores. More accurate than bag of words.

## What I Learned

- Representing text data as numbers for machine learning
- Bag of words vectorization from scratch
- TF-IDF vectorization using scikit-learn
- Training a Logistic Regression classifier
- Why TF-IDF outperforms bag of words for text classification
- Building an interactive prediction interface

## Tech Stack

- Python
- scikit-learn

## Usage

Run either script and type any message when prompted. The model will classify it as SPAM or NOT SPAM.

## Dataset

Based on the [UCI SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) available on Kaggle.

## Roadmap

- Train on the full 5500 message Kaggle dataset
- Add model accuracy evaluation
- Try Naive Bayes classifier and compare results
