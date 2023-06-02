# First, pip install zemberek-python, and be sure NLTK is downloaded
# nltk.download("punkt") IMPORTANT
# I run the code on Colab 'cause it throws some verification error for nltk.download

import nltk
from nltk.metrics.distance import edit_distance
from zemberek.morphology import TurkishMorphology
from zemberek.normalization import TurkishSentenceNormalizer
from nltk.translate.bleu_score import sentence_bleu

# Create TurkishMorphology and TurkishSentenceNormalizer instances
turkish_morphology = TurkishMorphology.create_with_defaults()
sentence_normalizer = TurkishSentenceNormalizer(turkish_morphology)

# Read English sentences from txt file
english_file_path = '/content/drive/MyDrive/colab_notebooks/english_sentences.txt'
with open(english_file_path, 'r', encoding='utf-8') as file:
    english_sentences = file.read().splitlines()

# Read Azerbaijani sentences from txt file
azerbaijani_file_path = '/content/drive/MyDrive/colab_notebooks/azerbaijani_sentences.txt'
with open(azerbaijani_file_path, 'r', encoding='utf-8') as file:
    azerbaijani_sentences = file.read().splitlines()

# Read Turkish sentences from txt file
turkish_file_path = '/content/drive/MyDrive/colab_notebooks/turkish_sentences.txt'
with open(turkish_file_path, 'r', encoding='utf-8') as file:
    turkish_sentences = file.read().splitlines()

# Preprocess the parallel corpus
def preprocess_corpus(corpus, language):
    preprocessed_corpus = []
    if language == 'english' or language == 'azerbaijani':
        for sentence in corpus:
            tokens = nltk.word_tokenize(sentence.lower())
            preprocessed_corpus.append(tokens)
    elif language == 'turkish':
        for sentence in corpus:
            normalized_sentence = sentence_normalizer.normalize(sentence)
            tokens = nltk.word_tokenize(normalized_sentence.lower())
            preprocessed_corpus.append(tokens)
    return preprocessed_corpus

english_corpus = preprocess_corpus(english_sentences, 'english')
azerbaijani_corpus = preprocess_corpus(azerbaijani_sentences, 'azerbaijani')
turkish_corpus = preprocess_corpus(turkish_sentences, 'turkish')

# Translate a sentence using example-based machine translation
def translate_example_based(input_sentence, source_corpus, target_corpus):
    input_tokens = nltk.word_tokenize(input_sentence.lower())

    # Calculate edit distance between input sentence and source corpus sentences
    distances = [edit_distance(input_tokens, source_sentence) for source_sentence in source_corpus]

    # Find the index of the most similar sentence in the source corpus
    most_similar_index = distances.index(min(distances))

    # Retrieve the translation from the target corpus based on the most similar index
    translated_sentence = target_corpus[most_similar_index]

    return ' '.join(translated_sentence)

# Calculate BLEU score
def calculate_bleu_score(reference_sentence, translated_sentence):
    reference_tokenized = nltk.word_tokenize(reference_sentence.lower())
    translated_tokenized = nltk.word_tokenize(translated_sentence.lower())

    bleu_score = sentence_bleu([reference_tokenized], translated_tokenized)

    return bleu_score

# User interface
while True:
    print("Select an option:")
    print("1. English to Turkish")
    print("2. Azerbaijani to Turkish")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        english_input = input("Enter the English sentence: ")
        translated_sentence = translate_example_based(english_input, english_corpus, turkish_corpus)
        print("Translated Sentence: ", translated_sentence)

        # Calculate BLEU score
        bleu_score = calculate_bleu_score(english_input, translated_sentence)
        print("BLEU score:", bleu_score)

        print()
    elif choice == '2':
        azerbaijani_input = input("Enter the Azerbaijani sentence: ")
        translated_sentence = translate_example_based(azerbaijani_input, azerbaijani_corpus, turkish_corpus)
        print("Translated Sentence: ", translated_sentence)

        # Calculate BLEU score
        bleu_score = calculate_bleu_score(azerbaijani_input, translated_sentence)
        print("BLEU score:", bleu_score)

        print()
    elif choice == '3':
        break
    else:
        print("Invalid choice! Please try again.")
        print()