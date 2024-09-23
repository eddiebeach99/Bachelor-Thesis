import numpy as np
import pandas as pd
from cblearn import embedding
from cblearn.utils import check_query_response
import os
from scipy.spatial import procrustes
from sklearn.model_selection import cross_val_score

# File used to calculate the ordinal embeddings for every observer and shape them into the same rotation etc. using
# Procrustes analysis.
# Requires a folder "data" with the csv files containing the triplet responses.

normalized_embedding = [[-0.30170582, -0.18968031],[-0.13701692, -0.1736228 ],[-0.15170852, -0.03689704],
 [-0.0987218 ,  0.02951734],[-0.07972667,  0.09933883],[-0.09559275,  0.17502198],[-0.20017074, -0.14242876],
 [-0.09548105, -0.01364718],[-0.16222805,  0.12576842],[-0.02912437,  0.16759295],[ 0.00969762,  0.25271042],
 [ 0.11240998,  0.24219516],[-0.09988449, -0.03713647],[-0.145839  ,  0.16743633],[ 0.04598066,  0.2756582 ]]

path = os.getcwd()+'/data'


def calculate_embedding(csv_file,subject, session):

    data = pd.read_csv(csv_file, na_values='NaN')
    data = data.dropna(subset=['BB_Trial.resp'])
    triplets = data[['index_middle', 'index_left', 'index_right']].values
    responses = data['BB_Trial.resp'].map({'left': 1, 'right': -1}).values
    triplet_response = check_query_response(triplets, responses, result_format='list-order')
    soe = embedding.SOE(n_components=2, n_init=10)
    embedding_unnormed = soe.fit_transform(triplet_response)  # setOfTriplets
    mtx1, normed_embedding, disparity = procrustes(normalized_embedding, embedding_unnormed)
    embedding_df = pd.DataFrame(normed_embedding, columns=["x", "y"])
    filename = f"embedding_sub{subject}_sess{session}.csv"
    filepath = os.path.join(os.getcwd(), "embeddings", filename)

    embedding_df.to_csv(filepath, index=False)


# Range should be the amount of files in the "data" dictionary
for i in range(64):
    files = os.listdir(path)
    file_i = files[i]
    full_path_i = os.path.join(path, file_i)

    # Depending on the naming convention of the data files this has to be changed.
    subject = file_i.split("obs")[1].split("_")[0]
    session = file_i.split("sess")[1].split("_")[0]

    calculate_embedding(full_path_i, subject, session)


