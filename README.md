# Language Modelling

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sayarghoshroy/Language-Modelling/blob/master/language_modelling.ipynb)

## Tokenizer implemented using *regex*-es from scratch
- Considered apostrophes as separate tokens
- Currency of the form Rs. and $ has been taken care of
- Standard email ids, URLs, Hashtags # and mentions @ are also being handled

## Implementation of language modelling algorithm
- Kneser-Ney Smoothing
- Interpolation
- *N*-grams upto order 6 have been considered
- corpus3.txt contains sentences in standard English
- corpus4.txt contains assorted tweets
- The language model gets stored in a file named "LM"

## Visualization of Word Frequency v/s Word Occurence Rank
- Resembles a Zipf's Distribution for most analytic languages
- Graph for a selected corpus can be constructed
- In the present setting:
    1. The first graph considers the top-1000 ranked tokens
    2. The second graph considers 10001 to 11000 ranked words in the corpus

## Computation of Model Perplexity Scores
- Enter a **test_corpus** to generate the perplexity scores for each sentence
- For the comparison of language models, the average perplexity scores across all sentences in the **test_corpus** is considered

## Sentence Generation
- The maximum *N* parameter for used *N*-gram models can be varied