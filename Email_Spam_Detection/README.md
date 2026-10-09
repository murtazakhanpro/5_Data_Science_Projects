# SMS Spam Detection

TF-IDF text classification with class-aware evaluation

## Project overview

This project builds a text classification pipeline for spam versus legitimate SMS messages using the supplied SMS Spam Collection CSV.

## Data

After dropping exact duplicate messages, the working data has 5,169 records: 4,516 ham (87.37%) and 653 spam (12.63%). The source columns are v1 (label) and v2 (message).

## Workflow

Lowercased text, removed punctuation and English stopwords, and transformed text with word and bigram TF-IDF. Compared Multinomial Naive Bayes with class-weighted Logistic Regression on a stratified 80/20 holdout set. Reported accuracy, spam precision, spam recall, spam F1, classification report, and confusion matrices.

## Results

Logistic Regression was selected by spam F1: accuracy 0.977, spam precision 0.928, spam recall 0.885, and spam F1 0.906. Naive Bayes reached accuracy 0.968, spam precision 1.000, spam recall 0.748, and spam F1 0.856. Recall matters because missed spam reaches the user; false positives can hide legitimate messages.

## Limitations

The evaluation uses one random split of a historical SMS dataset. It does not establish performance on modern email, new scam patterns, or a different user population. Threshold selection should reflect the cost of false positives and false negatives.

## Run the notebook

Open sms-spam-collection-dataset.ipynb in Jupyter and run all cells. Keep spam.csv in this folder.

## Project files

- `sms-spam-collection-dataset.ipynb` - executable analysis, visualizations, and results
- `Project_Documentation.pdf` - project summary with selected analysis visuals
- Source CSV files are noted above when the project uses local data.
