
import os
import subprocess
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

def fasta_to_newick(fasta_file, muscle_path, output_file):
    # Define the output alignment file
    alignment_file = fasta_file.replace('.fasta', '.aln')
    
    # Run MUSCLE for alignment
    muscle_command = f'{muscle_path} -in "{fasta_file}" -out "{alignment_file}"'
    result = subprocess.run(muscle_command, shell=True, capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print(f"Error running MUSCLE: {result.stderr}")
        return None
    
    # Read the alignment output
    alignment = AlignIO.read(alignment_file, "fasta")
    
    # Calculate distance matrix
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)
    
    # Construct the tree
    constructor = DistanceTreeConstructor(calculator, 'nj')
    tree = constructor.build_tree(alignment)
    
    # Convert the tree to Newick format
    newick_tree = tree.format('newick')
    # Save the Newick tree to a text file
    with open(output_file, "w") as f:
        f.write(newick_tree)
    return newick_tree

# Define paths
fasta_file = os.path.expanduser("~/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N.fasta")
muscle_path = "muscle"  # MUSCLE should be in your PATH
output_file = os.path.expanduser("~/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N_newick.txt")

# Generate Newick tree and save to file
newick_tree = fasta_to_newick(fasta_file, muscle_path, output_file)
if newick_tree:
    print(f"Newick tree has been written to {output_file}")
Newick tree has been written to /home/local/USHERBROOKE/farm2103/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N_newick.txt
import os
import re

# Set the input and output file paths
input_path = os.path.expanduser("~/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N_newick.txt")
output_path = os.path.expanduser("~/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N_newick_cleaned.txt")

# Function to remove "Inner" and the following number
def remove_inner(text):
    return re.sub(r'Inner\d+', '', text)

# Read the input file, process it, and write to the output file
with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
    for line in infile:
        cleaned_line = remove_inner(line)
        outfile.write(cleaned_line)

print(f"Processed Newick file.")
print(f"Cleaned output saved to: {output_path}")
Processed Newick file.
Cleaned output saved to: /home/local/USHERBROOKE/farm2103/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N_newick_cleaned.txt
import os

# Define file paths
base_path = os.path.expanduser("~/1.mahsa.farnia/OneDrive_1_13-07-2024")
fasta_file = os.path.join(base_path, "D3-N.fasta")
output_file = os.path.join(base_path, "D3-N_sequence.txt")

def extract_sequence_counts(fasta_file):
    sequence_counts = []
    with open(fasta_file, 'r') as f:
        seq_id = ""
        seq_count = ""
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                seq_id = line
            elif line.startswith('count:'):
                seq_count = line.split(':')[-1].strip()
                sequence_counts.append(f"{seq_id}@{seq_count}")
    return sequence_counts

def write_sequence_counts(sequence_counts, output_file):
    with open(output_file, 'w') as f:
        for entry in sequence_counts:
            f.write(f"{entry}\n")

# Extract sequence counts from FASTA file
sequence_counts = extract_sequence_counts(fasta_file)

# Write sequence counts to the output file
write_sequence_counts(sequence_counts, output_file)

print(f"Sequence counts have been written to {output_file}")
Sequence counts have been written to /home/local/USHERBROOKE/farm2103/1.mahsa.farnia/OneDrive_1_13-07-2024/D3-N_sequence.txt
import os
import re

# Define file paths
base_path = os.path.expanduser("~/1.mahsa.farnia/OneDrive_1_13-07-2024")
sequence_file = os.path.join(base_path, "D3-N_sequence.txt")
newick_file = os.path.join(base_path, "D3-N_newick_cleaned.txt")
output_file = os.path.join(base_path, "weighted_newick_D3-N.txt")

def load_sequence_counts(sequence_file):
    sequence_counts = {}
    with open(sequence_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                # Split the line on '@' to separate the sequence ID from the count
                seq_id, count = line.split('@')
                sequence_counts[seq_id.strip('>')] = count
    return sequence_counts

def update_newick_with_counts(newick_file, sequence_counts, output_file):
    with open(newick_file, 'r') as f:
        newick_content = f.read()
    
    # Replace each sequence ID with the new format (e.g., seq31 -> seq31@182)
    for seq_id, count in sequence_counts.items():
        newick_content = re.sub(rf'\b{seq_id}\b', f'{seq_id}@{count}', newick_content)
    
    # Write the updated Newick format to the output file
    with open(output_file, 'w') as f:
        f.write(newick_content)

# Load sequence counts from the sequence file
sequence_counts = load_sequence_counts(sequence_file)

# Update Newick file with sequence counts
update_newick_with_counts(newick_file, sequence_counts, output_file)

print(f"Updated Newick format has been written to {output_file}")
 
