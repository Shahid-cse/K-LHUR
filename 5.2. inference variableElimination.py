from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ExpectationMaximization as EM
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from pgmpy.inference import BeliefPropagation
import pandas as pd
import pickle
import multiprocessing
from functools import partial
import numpy as np
from joblib import Parallel, delayed


output_dir = "D:/Thesis/files_output_dir/output_files/"
road_data= pd.read_csv(output_dir +'PGM_input_discrete_level3_road_history_holiday.csv')
data = road_data.copy()

# Load the model
with open(output_dir + 'bayesian_network_model_level3_holiday.pkl', 'rb') as file:
    model = pickle.load(file)


# Retrieve and print the learned CPDs
for cpd in model.get_cpds():
    print(f"Learned CPD for {cpd.variable}:")
    print(cpd)
    print("\n")


inference = VariableElimination(model)

# Initialize new columns for inferred latent variables in the dataset
road_data['theta'] = np.nan
road_data['Volume'] = np.nan

def process_chunk(chunk):
    """Function to process a chunk of rows and perform inference."""
    results = []
    for index, row in chunk.iterrows():
        # Extract observed evidence from the current row as a dictionary
        evidence = {
            'length': row['length'],
            'lanes': row['lanes'],
            'max_speed': row['max_speed'],
            'dir': row['dir'],
            'tor': row['tor'],
            'n_connnections': row['n_connnections'],
            'weighted_POI': row['weighted_POI'],
            'time': row['time'],
            'no_taxi_car': row['no_taxi_car'],
            'avg_speed': row['avg_speed'],
            'avg_speed std': row['avg_speed std']
        }
        
        # Remove NaN values from the evidence dictionary
        evidence = {k: v for k, v in evidence.items() if not pd.isna(v)}

        # Perform MAP query to find the most likely value of latent nodes
        try:
            result_theta = inference.map_query(variables=['theta'], evidence=evidence)
            result_volume = inference.map_query(variables=['Volume'], evidence=evidence)
        except Exception as e:
            # If inference fails, return NaNs
            result_theta = {'theta': np.nan}
            result_volume = {'Volume': np.nan}

        # Collect the results
        results.append((index, result_theta.get('theta', np.nan), result_volume.get('Volume', np.nan)))
    
    return results


# Split data into chunks for parallel processing
num_chunks = 6 #multiprocessing.cpu_count()
data_chunks = np.array_split(road_data, num_chunks)

# Use multiprocessing Pool to parallelize the inference process
with multiprocessing.Pool(processes=num_chunks) as pool:
    # Map the process_chunk function across the data chunks in parallel
    chunk_results = pool.map(process_chunk, data_chunks)

# Flatten the list of results
results = [item for sublist in chunk_results for item in sublist]

# Update the DataFrame with results
for index, theta, volume in results:
    road_data.at[index, 'theta'] = theta
    road_data.at[index, 'Volume'] = volume


file_path = "D:/Thesis/files_output_dir/output_files/level3_road_history_holiday_inference.csv"
road_data.to_csv(file_path, index=False)