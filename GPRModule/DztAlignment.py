import os
import numpy as np
import scipy.io as sio
from readgssi import readgssi

def read_dzt_files(dir_path):
    dzt_files = [f for f in os.listdir(dir_path) if f.endswith('.DZT')]
    data_list = []

    for file in dzt_files:
        file_path = os.path.join(dir_path, file)
        data = read_dzt_file(file_path)  # Assuming a function to read .dzt files
        data_list.append(data)
    
    if not data_list:
        raise ValueError("data_list is empty. Ensure the directory contains .dzt files.")
    
    min_length = min([d[0].shape[1] for d in data_list])
    # Reshape data to have dimensions: (rows, columns, slices)
    aligned_data = np.array([d[0][:, :min_length] for d in data_list])
    aligned_data = np.transpose(aligned_data, (1, 2, 0))
    
    print(f"Final data dimensions (rows, columns, slices): {aligned_data.shape}")
    return aligned_data

def save_data(data, output_path, file_type='mat'):
    if file_type == 'mat':
        sio.savemat(output_path, {'data': data})
    elif file_type == 'npy':
        np.save(output_path, data)
    else:
        raise ValueError("Unsupported file type. Use 'mat' or 'npy'.")

def read_dzt_file(file_path):
    hdr, arrs, gps = readgssi.readgssi(infile=file_path)
    return arrs

# Example usage
dir_path = '/Users/Xuan/Data/0519下午_东侧树_193-310/dzt/S2N'
output_path = '/Users/Xuan/Data/0519下午_东侧树_193-310/dzt/E2W/0519下午_东侧树_S2N_dzt.mat'
aligned_data = read_dzt_files(dir_path)
save_data(aligned_data  output_path, file_type='mat')
