# Reddit Topics Dataset

A comprehensive dataset of categorized Reddit posts using advanced topic modeling techniques.

## Overview

This project processes and categorizes Reddit posts from the Pushshift dataset using BERTopic, transforming 1.7 billion unstructured posts into 43 million categorized entries. Instead of relying solely on subreddit categorization, this approach provides a more nuanced and cross-subreddit topic analysis.

## Methodology

### Data Processing Pipeline

The project uses BERTopic for topic modeling with the following steps:

1. **Text Embedding**: 
   - Utilizes BERT to generate vector representations of posts
   - Captures semantic meaning in high-dimensional space

2. **Dimensionality Reduction**:
   - Implements UMAP to reduce vectors to 5 dimensions
   - Optimizes clustering efficiency

3. **Clustering**:
   - Applies HDBSCAN for density-based clustering
   - Identifies topic clusters while filtering noise

4. **Topic Identification**:
   - Uses c-TF-IDF to extract important words per cluster
   - Leverages ChatGPT for human-readable topic naming

### Technical Challenges

The project addressed several technical challenges:
- Processing 1.7B posts efficiently
- Managing memory constraints
- Optimizing computational resources

Solutions implemented:
- GPU-accelerated processing for UMAP and HDBSCAN
- Representative subset modeling strategy
- Optimized memory management techniques

## Features

- Cross-subreddit topic analysis
- Semantic-based categorization
- Scalable processing pipeline
- GPU-optimized implementations

## Advantages Over Traditional Methods

- Goes beyond simple subreddit categorization
- Handles multi-topic content in large subreddits
- Identifies topics spanning multiple subreddits
- Provides more accurate content categorization

## Project Implementation

The final dataset represents a reduction from 1.7 billion to 43 million posts, ensuring quality and manageability while maintaining comprehensive coverage of Reddit content.

## Acknowledgments

This project was developed during a summer internship at ETH Zurich's Computational Social Science Lab under the supervision of Andrea Musso.

## Contact

viel.stefano01 [at] gmail.com
