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

Dependency grammar (DG) is a class of modern syntactic theories that are all based on the dependency relation (as opposed to the constituency relation) and that can be traced back primarily to the work of Lucien Tesnière. Dependency is the notion that linguistic units, e.g. words, are connected to each other by directed links. The (finite) verb is taken to be the structural center of clause structure. All other syntactic units (words) are either directly or indirectly connected to the verb in terms of the directed links, which are called dependencies. DGs are distinct from phrase structure grammars (constituency grammars), since DGs lack phrasal nodes, although they acknowledge phrases. Structure is determined by the relation between a word (a head) and its dependents. Dependency structures are flatter than constituency structures in part because they lack a finite verb phrase constituent, and they are thus well suited for the analysis of languages with free word order, such as Czech, Slovak, Turkish, and Warlpiri.

### Dependency Parsing

Syntactic Parsing or Dependency Parsing is the task of recognizing a sentence and assigning a syntactic structure to it. The most widely used syntactic structure is the parse tree which can be generated using some parsing algorithms. These parse trees are useful in various applications like grammar checking or more importantly it plays a critical role in the semantic analysis stage. For example to answer the question “Who is the point guard for the LA Laker in the next game ?” we need to figure out its subject, objects, attributes to help us figure out that the user wants the point guard of the LA Lakers specifically for the next game.

### Discourse

The objects of discourse analysis (discourse, writing, conversation, communicative event) are variously defined in terms of coherent sequences of sentences, propositions, speech, or turns-at-talk. Contrary to much of traditional linguistics, discourse analysts not only study language use 'beyond the sentence boundary' but also prefer to analyze 'naturally occurring' language use, not invented examples.[1] Text linguistics is a closely related field. The essential difference between discourse analysis and text linguistics is that discourse analysis aims at revealing socio-psychological characteristics of a person/persons rather than text structure.[2]

### Document Term Matrix (DTM)

It is a matrix that represents the the frequency distributions of each word in different documents of a corpus. In this matrix, the count of every time a word appeared in a document is presented. 

### IDF

Inverse Document Frequency is the method to calculate the 

### Keyword

Also known as tokens or words 

### Languge Model

A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length m, it assigns a probability {\displaystyle P(w_{1},\ldots ,w_{m})} to the whole sequence. Having a way to estimate the relative likelihood of different phrases is useful in many natural language processing applications, especially ones that generate text as an output. Language modeling is used in speech recognition, machine translation, part-of-speech tagging, parsing, handwriting recognition, information retrieval and other applications.

### LDA

In natural language processing, latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar. For example, if observations are words collected into documents, it posits that each document is a mixture of a small number of topics and that each word's creation is attributable to one of the document's topics. LDA is an example of a topic model and was first presented as a graphical model for topic discovery by David Blei, Andrew Ng, and Michael I. Jordan in 2003.[1] Essentially the same model was also proposed independently by J. K. Pritchard, M. Stephens, and P. Donnelly in the study of population genetics in 2000.[2] Both papers have been highly influential, with 19858 and 20416 citations respectively by August 2017.[3][4]

### Lemmatization

Lemmatization is an organized & step by step procedure of obtaining the root form (lemma) of the lexicon. It makes use of vocabulary (dictionary importance of words) and morphological analysis (word structure and grammar relations) to derive the normalized form of a lexicon ( a word)

### Levenshtein Distance

Levenshtein distance (LD) is a measure of the similarity between two strings, which we will refer to as the source string (s) and the target string (t). The distance is the number of deletions, insertions, or substitutions required to transform s into t. For example,

### Lexicon

the vocabulary of a person, language, or branch of knowledge.

### Linguistics

Linguistics is the scientific study of language, and involves an analysis of language form, language meaning, and language in context.

### LSA

Latent semantic analysis (LSA) is a technique in natural language processing, in particular distributional semantics, of analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. LSA assumes that words that are close in meaning will occur in similar pieces of text (the distributional hypothesis). A matrix containing word counts per paragraph (rows represent unique words and columns represent each paragraph) is constructed from a large piece of text and a mathematical technique called singular value decomposition (SVD) is used to reduce the number of rows while preserving the similarity structure among columns. Words are then compared by taking the cosine of the angle between the two vectors (or the dot product between the normalizations of the two vectors) formed by any two rows. Values close to 1 represent very similar words while values close to 0 represent very dissimilar words.[1]

### Machine Translation

Process of translating the text from one language to other by the means of learning algorithms and models. 

### Morpheme

a meaningful morphological unit of a language that cannot be further divided (e.g. in, come, -ing, forming incoming ).

### Morpohological Analysis

Morphology is the study of word formation – how words are built up from smaller pieces

### Named Entity

Named entitites are the proper nouns which posses a specific property such as - location, organization, person name etc. 

### NLG

Natural language generation (NLG) is the natural language processing task of generating natural language from a machine representation system such as a knowledge base or a logical form. Psycholinguists prefer the term language production when such formal representations are interpreted as models for mental representations.

### NER

Named entity recognition is the process of identifying the named entities from a textual data 

### Ngram

N grams are the combinations of N words together 

### NLU

Natural language understanding (NLU) is a subtopic of natural language processing in artificial intelligence that deals with machine reading comprehension. NLU is considered an AI-hard problem.[1]

### OCR

Optimal Character Recognition is the process of identifying the characters from an image containing the textual forms.

### Part Of Speech Tag

every word in a sentence is also associated with a part of speech (pos) tag (nouns, verbs, adjectives, adverbs etc). The pos tags defines the usage and function of a word in the sentence.

### Phonetic Matchin

A phonetic algorithm is an algorithm for indexing of words by their pronunciation. Most phonetic algorithms were developed for use with the English language[citation needed]; consequently, applying the rules to words in other languages might not give a meaningful result.

### Phonology

Phonology is a branch of linguistics concerned with the systematic organization of sounds in languages.

### Pragmatics

Pragmatics is a subfield of linguistics and semiotics that studies the ways in which context contributes to meaning. Pragmatics encompasses speech act theory, conversational implicature, talk in interaction and other approaches to language behavior in philosophy, sociology, linguistics and anthropology.

### Question Answering

Question answering (QA) is a computer science discipline within the fields of information retrieval and natural language processing (NLP), which is concerned with building systems that automatically answer questions posed by humans in a natural language.

### Regular Expression

A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern. Usually this pattern is then used by string searching algorithms for "find" or "find and replace" operations on strings.

### Semantics

the branch of linguistics and logic concerned with meaning. The two main areas are logical semantics, concerned with matters such as sense and reference and presupposition and implication, and lexical semantics, concerned with the analysis of word meanings and relations between them.

### Sentiment Analysis

Process of detecting the tone or sentiment of a sentence / textual document

### Seq2Seq

tf-seq2seq is a general-purpose encoder-decoder framework for Tensorflow that can be used for Machine Translation, Text Summarization, Conversational Modeling, Image Captioning, and more.

### Skip-Gram

it takes every word in a large corpora (we will call it the focus word) and also takes one-by-one the words that surround it within a defined ‘window’ to then feed a neural network that after training will predict the probability for each word to actually appear in the window around the focus word.

### Speech To Text

Process of convering the speech to textual data

### Stemming

Stemming is a rudimentary rule-based process of normalization of tokens by stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from them in step by step manner.

### Stopwords

commonly used words of a language are termed as stop words

### Summarization

Automatic summarization is the process of shortening a text document with software, in order to create a summary with the major points of the original document. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax.

### Syntactical Parsing

syntactic analysis is the process of analysing a string of symbols, either in natural language or in computer languages, conforming to the rules of a formal grammar

### Tdm

Any corpus can be represented in the form of Term Document Matrix in which every row repersents terms (words) and every column repersents documents, and every cell value repersents the count of a term in a document

### Text Classification

Process of classigying a text element into one or more classes through the process of rule based learning, unsupervised or supervised learning.

### Text Cleaning

Process of removing noise from a text data which includes normalization, removal of stopwords and standardization of keywords. 

### Text Clustering

Process of grouping together the documents of texts into fixed sets of clusters

### Text Mining

Process of analysis of text data by the means of natural language processing and identifign meaningful information from the data 

### Text To Speech

Process of convering the textual data into speech

### Tf

TF for a term “t” is defined as the count of a term “t” in a document “D”

### Thought Vectors

They are a way of embedding thoughts in vector space. Thought vectors are numerical columns, like word vectors. Their features will represent how each thought relates to other thoughts.

### Token

Tokens are defined as the elemental forms of a corpus which are also known as words

### Tokenization

Tokenization is the process of generating tokens (or words) from a corpus (such as a document, paragraph, or sentence)

### Topic Modeling

Topic Modelling is an unsupervised learning approach used for identifying the most significant group of words (called “topics”) in large clusters of texts. It uses frequency distributions, probabilities of two words occuring together, and the position of the repeated words in the corpus.

### Trigram

Trigrams are defined as the collection of three tokens together. 

### Unigram

Unigrams are defined as the one word tokens

### Word Embedding

Word embedding is the feature learning techniques in natural language processing (NLP) where words or phrases from the vocabulary are mapped to vectors of real numbers. The process of generating word embedding involves a mathematical embedding from a space with one dimension per word to a continuous vector space with much lower dimension.

### Word Sense Disambigution

Word Sense Disambigution (WSD) is an open problem of the linguistic domain which deals with identification of true meaning (or context) of a word / token used in the corpus. Many words have different meanings according to their useage in the sentences, WSD is the problem of identifiying the true meanuinng of a word used in a particular sentence.

### Word2Vec

Word2vec is a shallow two layered neural network model that processes text courpus as input and produces set of word vectors as output. It turns text into a numerical form that deep neural networks can understand. It uses preprocessing, skip gram model, and continuous bag of words model to generate the vector representations of the words which are also known as word embeddings. 

### Lemma

In morphology and lexicography, a lemma (plural lemmas or lemmata) is the canonical form, dictionary form, or citation form of a set of words (headword).

### Vocabulary

the body of words used in a particular language.

### Constituency Parsing

A constituency parse tree breaks a text into sub-phrases. Non-terminals in the tree are types of phrases, the terminals are the words in the sentence, and the edges are unlabeled. For a simple sentence "John sees Bill", a constituency parse would be:

### Context Free Grammars

In formal language theory, a context-free grammar is a certain type of formal grammar: a set of production rules that describe all possible strings in a given formal language. Production rules are simple replacements. Wikipedia

### Non-Probabilistic Parsing

Grammar theory to model symbol strings originated from work in computational linguistics aiming to understand the structure of natural languages.[1][2][3] Probabilistic context free grammars (PCFGs) have been applied in probabilistic modeling of RNA structures almost 40 years after they were introduced in computational linguistics.[4][5][6][7][8]

### Hidden Markov Models

Hidden Markov Model (HMM) is a statistical Markov modelin which the system being modeled is assumed to be aMarkov process with unobserved (i.e. hidden) states. Thehidden Markov model can be represented as the simplest dynamic Bayesian network. The mathematics behind theHMM were developed by L. E.

### Lexical Semantics

the branch of linguistics and logic concerned with meaning. The two main areas are logical semantics, concerned with matters such as sense and reference and presupposition and implication, and lexical semantics, concerned with the analysis of word meanings and relations between them.

### Cky Parsing

In computer science, the Cocke–Younger–Kasami algorithm (alternatively called CYK, or CKY) is a parsing algorithm for context-free grammars, named after its inventors, John Cocke, Daniel Younger and Tadao Kasami. It employs bottom-up parsing and dynamic programming.

### Sentence Compression

similar to text summarization

### Text Rank

The unsupervised approach to summarization is also quite similar in spirit to unsupervised keyphrase extraction and gets around the issue of costly training data. Some unsupervised summarization approaches are based on finding a "centroid" sentence, which is the mean word vector of all the sentences in the document. Then the sentences can be ranked with regard to their similarity to this centroid sentence.

### Text Generation

similar to natural language generation

### Dtm

similar to TDM

### Soundex

Soundex is a phonetic algorithm for indexing names by sound, as pronounced in English. The goal is for homophones to be encoded to the same representation so that they can be matched despite minor differences in spelling.

### Methaphone

Metaphone is a phonetic algorithm, published by Lawrence Philips in 1990, for indexing words by their English pronunciation.

### Dependency Tree

Dependency grammar (DG) is a class of modern syntactic theories that are all based on the ... Thisdependency tree is an "ordered" tree, i.e. it reflects actual word order. Many dependency treesabstract away from linear order and focus just on ...

### Polysemy

Polysemy (/pəˈlɪsɪmi/ or /ˈpɒlɪsiːmi/; from Greek: πολυ-, poly-, "many" and σῆμα, sêma, "sign") is the capacity for a sign (such as a word, phrase, or symbol) to have multiple meanings (that is, multiple semes or sememes and thus multiple senses), usually related by contiguity of meaning within a semantic field.

### Dictionary

collection of words and context

### Homonymy

The relationship between a set of homonyms is called homonymy. Examples of homonyms are the pair stalk (part of a plant) and stalk (follow/harass a person) and the pair left (past tense of leave) and left (opposite of right).

### Synonymy

the state of being synonymous.

### Cosine Similarity

Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Thecosine of 0° is 1, and it is less than 1 for any other angle.

### Edit Distance

In computational linguistics and computer science,edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other.


## Machine Learning
## Deep Learning
## Statistics