import os
import time

# add timestamp to not have same experiments with overlapping names
timestamp = time.strftime("%Y%m%d_%H%M%S") 

OUTPUT_DIR = "/media/data/stviel/RedditPolarization/output/testing_pipeline"  # where the experiment outputs will be saved

# where to get the data from
REDDIT_DATA_DIR = 'data'

# Database configuration and parameters for filtering
REDDIT_DB_FILE = os.path.join(OUTPUT_DIR, "dbs/duck_db.db")
os.mkdir(os.path.join(OUTPUT_DIR, "dbs"))
TABLE_NAME = 'submissions'
MIN_SCORE = 10
MIN_POST_LENGTH = 20

# Embeddings 
EMBEDDINGS_FILE = os.path.join(OUTPUT_DIR, "embeddings/embeddings.h5")
os.mkdir(os.path.join(OUTPUT_DIR, "embeddings"))
MODEL_NAME = 'all-MiniLM-L6-v2' 

# Dimensionality reduction 
DIMENSIONALITY_REDUCTION_FILE = os.path.join(OUTPUT_DIR, "embeddings/dimensional_reduction.h5")
UMAP_COMPONENTS = 5
UMAP_N_Neighbors = 50
UMAP_MINDIST = 0.01
PARTIAL_FIT_SAMPLE_SIZE = 0.1
