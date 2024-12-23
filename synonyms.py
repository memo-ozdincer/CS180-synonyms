import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    '''Compute the cosine similarity between two sparse vectors
    represented as dictionaries.
    '''
    dot_product = 0.0
    for key in vec1:
        if key in vec2:
            dot_product += vec1[key] * vec2[key]
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return -1
    else:
        return dot_product / (norm1 * norm2)

def build_semantic_descriptors(sentences):
    '''Build semantic descriptors for all words in the given sentences.
    sentences is a list of lists of words.
    Returns a dictionary mapping words to their semantic descriptor dictionaries.
    '''
    d = {}
    for sentence in sentences:
        words_in_sentence = set(sentence)
        for w in words_in_sentence:
            if w not in d:
                d[w] = {}
            for co_word in words_in_sentence:
                if co_word != w:
                    if co_word in d[w]:
                        d[w][co_word] += 1
                    else:
                        d[w][co_word] = 1
    return d

def build_semantic_descriptors_from_files(filenames):
    '''Build semantic descriptors from the texts in the given files.
    filenames is a list of strings, each a filename.
    Returns a dictionary mapping words to their semantic descriptor dictionaries.
    '''
    text = ""
    for filename in filenames:
        with open(filename, "r", encoding="latin1") as f:
            text += f.read()
    # Replace sentence-ending punctuation with periods
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    text = text.lower()
    # Split text into sentences
    sentences = text.split('.')
    sentences_list = []
    punctuations_to_remove = [',', '-', '--', ':', ';']
    for sentence in sentences:
        for punc in punctuations_to_remove:
            sentence = sentence.replace(punc, ' ')
        words = sentence.split()
        if words:
            sentences_list.append(words)
    return build_semantic_descriptors(sentences_list)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Return the element of choices which has the highest semantic similarity
    to word, using the given semantic descriptors and similarity function.
    '''
    max_similarity = -1
    best_choice = choices[0]
    vec1 = semantic_descriptors.get(word, {})
    for choice in choices:
        vec2 = semantic_descriptors.get(choice, {})
        similarity = similarity_fn(vec1, vec2)
        if similarity > max_similarity:
            max_similarity = similarity
            best_choice = choice
    return best_choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''Run a synonym test and return the percentage of correct guesses.
    The test file should be in the specified format.
    '''
    correct = 0
    total = 0
    with open(filename, "r", encoding="latin1") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                word = parts[0]
                correct_answer = parts[1]
                choices = parts[2:]
                guessed_answer = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
                if guessed_answer == correct_answer:
                    correct += 1
                total += 1
    if total == 0:
        return 0.0
    else:
        return (correct / total) * 100
