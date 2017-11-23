# Data Science Terminology

## Natural Language Processing

### Anaphora

Anaphora is the use of a token which refers to another token used earlier in the corpus or a conversation flow. It indicates how relationships and links among the tokens are constructed in a sentence and binds the syntactical elements together. 

### Anaphora Resolution

The process of mapping the references of a token in a corpus is defined as anaphora resolution.

### Bag Of Words

A bag-of-words is a representation of text data that describes the distribution of words within a document. It involves a vocabulary of known words used in the entire corpus and the measure of presence of words in each document (by their count). The model is only concerned with whether known words occur in the document, not where in the document.

### Bigram

Bigrams are the keyphrases composed of two words only. In other terms, The combination of two keywords together are known as bigrams. For example, the bigrams in a sentence - "I love writing codes in Python" are "I love", "love writing", " writing codes", "codes in", "in Python".

### Chatbot

A chatbot is an algorithmic and intelligent model which conducts a conversation with user or another bot via auditory or textual methods. The models are designed to convincingly simulate how a human would behave as a conversational partner, thereby passing the Turing test. Chatbots are typically used in dialog systems for various practical purposes including customer service or information acquisition.

### Chunking

Chunking is also called shallow parsing and it is the process of identification of short phrases such as noun phrases and verb phrases from the text. 

### Computational Linguistic

Computational linguistics is field which is concerned with the statistical or rule-based modeling of natural language from a computational perspective. Also, It deals with the study of appropriate computational approaches to linguistic questions.

### Coreference Resolution

Coreference Resolution (or anaphora resolution) is a process of finding relational links among the words (or phrases) within the sentences. It is a techniuque to map the correct Noun entities of a pronoun used in a sentence. For example -  John went to School to meet Maria. He played Football with her. In this sentence, coreference resolution will identify that He is used for John and her is used for Maria.

### Corpus

Corpus is defined as the collection of text documents. A corpus can be as small as one sentence or as large as millions of documents. 

### Dependency Grammar

Dependency grammar (DG) is a class of modern syntactic theories that are all based on the dependency relation (as opposed to the constituency relation). Dependency is the notion that linguistic units, e.g. words, are connected to each other by directed links. The (finite) verb is taken to be the structural center of clause structure. All other syntactic units (words) are either directly or indirectly connected to the verb in terms of the directed links, which are called dependencies. DGs are distinct from phrase structure grammars (constituency grammars), since DGs lack phrasal nodes, although they acknowledge phrases. Structure is determined by the relation between a word (a head) and its dependents. 

### Dependency Parsing

Syntactic Parsing or Dependency Parsing is the task of recognizing a sentence and assigning a syntactic structure to it. The most widely used syntactic structure is the parse tree which can be generated using some parsing algorithms. These parse trees are useful in various applications like grammar checking or more importantly it plays a critical role in the semantic analysis stage.

### Discourse

The objects of discourse analysis (discourse, writing, conversation, communicative event) are variously defined in terms of coherent sequences of sentences, propositions, speech, or turns-at-talk. Contrary to much of traditional linguistics, discourse analysts not only study language use 'beyond the sentence boundary' but also prefer to analyze 'naturally occurring' language use, not invented examples.[1] Text linguistics is a closely related field. The essential difference between discourse analysis and text linguistics is that discourse analysis aims at revealing socio-psychological characteristics of a person/persons rather than text structure.[2]

### Document Term Matrix (DTM)

It is a matrix that represents the the frequency distribution of each word in different documents of a corpus. It is a mathematical matrix that describes the frequency of terms that occur in a collection of documents. In this matrix, rows correspond to documents in the collection and columns correspond to terms. 

### IDF

IDF measures how important a term is. While computing Term Frequency, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus IDF weighs down the frequent terms while scales up the rare ones using the following formula: 

IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

### Keyword

Keywords are the elements that are sewed together to create sentences and phrases. They are also known as tokens or words. 



## Machine Learning
## Deep Learning
## Statistics