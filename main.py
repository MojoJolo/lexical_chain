#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import wordnet as wn

NOUNS = ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']

def extractNouns(sentence):
  nouns = []

  text = nltk.word_tokenize(sentence)
  word_tags = nltk.pos_tag(text)

  for word_tag in word_tags:
    if word_tag[1] in NOUNS:
      nouns.append(word_tag)

  return nouns

def hasSimilarWords(sentence_noun, comparing_noun):
  for noun in sentence_noun:
    # print noun[0]
    # synonyms = []

    # for syn in wn.synsets(noun[0]):
    #   synonyms.extend(syn.lemma_names())

    # print list(set(synonyms))

    if noun in comparing_noun:
      return True

  return False

# def hasSynonyms():


sentences = [
  "Doctor Kenny has invented an anesthetic machine.",
  "This device controls the rate at which an anesthetic is pumped into the blood.",
  "The machine is awesome!",
  "The girl is fat.",
  "In this post, we’ll discuss the limitations of the HTTP GET method and what we decided to do about it in our own API.",
  "As a rule, HTTP GET requests should not modify server state."
]

sentence_nouns = []

for sentence in sentences:
  sentence = sentence.decode("utf-8", "ignore")
  nouns = extractNouns(sentence)
  print nouns
  
  sentence_nouns.append(nouns)

lexical_scores = {}

for i, sentence_noun in enumerate(sentence_nouns[:-1]):
  lex_key = "%d -> %d" % (i, i + 1)

  if hasSimilarWords(sentence_noun, sentence_nouns[i + 1]):
    lexical_scores[lex_key] = 1
  else:
    lexical_scores[lex_key] = 0

  print "%s: %d" % (lex_key, lexical_scores[lex_key])