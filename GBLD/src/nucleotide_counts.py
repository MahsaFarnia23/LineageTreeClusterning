
import os
import pandas as pd
from collections import defaultdict

# Define the directory containing the TSV files
directory_path = r'C:\Users\farm2103\.1.project\Data Set\public-bcell-dataset\D3-N'

# Initialize a dictionary to hold the nucleotide counts
nucleotide_counts = defaultdict(int)

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.tsv'):
        file_path = os.path.join(directory_path, filename)
        print(f"Processing file: {file_path}")
        
        # Load the TSV file into a pandas DataFrame
        df = pd.read_csv(file_path, sep='\t', comment='#')
        
        # Check if the 'nucleotide' column exists
        if 'nucleotide' in df.columns:
            # Count the occurrences of each nucleotide sequence
            for nucleotide in df['nucleotide']:
                nucleotide_counts[nucleotide] += 1

# Define the output file path
output_file_path = os.path.join(directory_path, '1.nucleotide_counts.txt')

# Save the nucleotide counts to the output file
with open(output_file_path, 'w') as output_file:
    for nucleotide, count in nucleotide_counts.items():
        output_file.write(f"{nucleotide}: {count}\n")

print(f"Nucleotide counts saved to '{output_file_path}'")
