import os
import time


# Experiment name (check if we're on the cluster or not)
if 'cluster' in os.getcwd():
    EXPERIMENT_NAME = "2008_2023"
    OUTPUT_DIR = os.path.join("/cluster/work/coss/stviel/output" , EXPERIMENT_NAME)
else: 
    EXPERIMENT_NAME = "testing_different_subsets"
    OUTPUT_DIR = os.path.join("output" , EXPERIMENT_NAME)

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

SEED = 42

# datasets names
if 'cluster' in os.getcwd():
    REDDIT_DATA_DIR = '/cluster/work/coss/anmusso/reddit_parquet/submissions/'
else:
    REDDIT_DATA_DIR = 'data/random_sample'
# REDDIT_DATA_DIR = 'data/parquet'
DATABASE_PATH = os.path.join(OUTPUT_DIR, "filtered_reddit_data.db")
PROCESSED_REDDIT_DATA = os.path.join(OUTPUT_DIR, "reddit_data.h5")

# Database configuration and parameters for filtering
TABLE_NAME = 'submissions'
MIN_SCORE = 10
MIN_POST_LENGTH = 40
START_DATE= 1199179770 # 2008-01-01
END_DATE= 1672531200 # 2023-01-01

# Embeddings 
EMBEDDING_DB_NAME = "embeddings"
IDS_DB_NAME = "ids"
MODEL_NAME = 'all-MiniLM-L6-v2' 
# number of samples to load on the gpu at once 
MODEL_BATCH_SIZE = 320_000  

# Dimensionality reduction 
DIMENSIONALITY_REDUCTION_DB_NAME = "dimensional_reduction"

if 'cluster' in os.getcwd():
    UMAP_MODEL_SAVE_PATH = os.path.join(OUTPUT_DIR, "umap_model.joblib")
else:
    UMAP_MODEL_SAVE_PATH = None  # if set to None, the model doesn't get saved or loaded
UMAP_COMPONENTS = 5
UMAP_N_Neighbors = 5 # increase this to get more global structure
UMAP_MINDIST = 0
PARTIAL_FIT_DIM_REDUCTION = 0.1
PARTIAL_TRANSFORM_DIM_REDUCTION = 0.1
NEGATIVE_SAMPLE_RATE = 5 # understand better what it 
LEARNING_RATE = 0.5
UMAP_N_EPOCHS = 1000

# clustering 
CLUSTER_DB_NAME =  "clusters"
SUBCLUSTER_DB_NAME = "subclusters"
HDBS_MIN_CLUSTERSIZE= 30
HDBS_MIN_SAMPLES = 30
HDBS_MIN_CLUSTERSIZE_SEARCH = [100] # [0.0005, 0.001, 0.005, 0.01]
HDBS_MIN_SAMPLES_SEARCH = [20] # [5, 10, 20]
PARTIAL_FIT_CLUSTER = 0.15  # it might not be used, depending on the employed function

# tfidf
TFIDF_MAX_FEATURES = 50_000  # Size of the vocabulary, None means no limitation
TFIDF_WORDS_PER_CLUSTER = 15
TFIDF_FILE = os.path.join(OUTPUT_DIR, "tfidf.json")
SUBCLUSTER_TFIDF_FILE = os.path.join(OUTPUT_DIR, "subcluster_tfidf.json")

# topic Naming
LLM_NAME = "gpt"
TOPIC_NAMING_FILE = os.path.join(OUTPUT_DIR, "topic_naming.json")

# hierarchical topic discovery
ADJACENCY_MATRIX = os.path.join(OUTPUT_DIR, "adjacency_matrix.h5")
RESOLUTION_PARAMETER = [0.5, 1, 1.5, 2]

# quiz & coherence
N_QUIZ = 100
NUM_RUNS = 5
NUMBER_OF_OPTIONS = 5
TEST_LLM_ACCURACY_FILE = os.path.join(OUTPUT_DIR, "test_llm_accuracy.json")

# final pandas dataframe
FINAL_DATAFRAME = os.path.join(OUTPUT_DIR, "final_dataframe.csv")