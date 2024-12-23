# Semantic Similarity Analyzer
**December 2024**

This is still ungraded, but it passed all test cases

![image](https://github.com/user-attachments/assets/507b46ba-692f-4f29-9046-c78ddf4496f4)


## Project Overview
A Python-based system that analyzes semantic similarity between words using computational linguistics techniques. The project can synonym questions by computing semantic relationships between words based on their co-occurrence in text.

## Features
- Builds semantic descriptors from text files
- Computes cosine similarity between word vectors
- Answers synonym questions
- Processes and analyzes large text corpuses
- Handles multiple text files simultaneously

## Core Components
### Semantic Descriptor Generation
- Creates word vectors based on sentence co-occurrence
- Handles various text formats and punctuation
- Implements efficient dictionary-based storage
- Processes multiple input files

### Similarity Computation
- Implements cosine similarity between word vectors
- Handles sparse vector representations
- Provides efficient computation for large vocabularies

## Key Functions
- `cosine_similarity(vec1, vec2)`: Computes similarity between vectors
- `build_semantic_descriptors(sentences)`: Creates word vectors from sentences
- `build_semantic_descriptors_from_files(filenames)`: Processes text files
- `most_similar_word(word, choices, semantic_descriptors, similarity_fn)`: Finds best synonym
- `run_similarity_test(filename, semantic_descriptors, similarity_fn)`: Evaluates accuracy

## Example Usage
```python
filenames = ["war_and_peace.txt", "swann's_way.txt"]
semantic_descriptors = build_semantic_descriptors_from_files(filenames)
res = run_similarity_test("test.txt", semantic_descriptors, cosine_similarity)
print(res, "% of the guesses were correct")
