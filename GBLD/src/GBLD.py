
import re
import os
from Bio import Phylo
from io import StringIO
import numpy as np

def parse_newick(newick):
    pattern = r'([^:@(),]+)@(\d+):([\d.]+)'
    matches = re.findall(pattern, newick)
    node_weights = {node: float(weight) for node, weight, _ in matches}
    return node_weights

def normalize_weights(weights_dict):
    all_weights = list(weights_dict.values())
    non_zero_weights = [w for w in all_weights if w != 0]
    if not non_zero_weights:
        return {node: 0 for node in weights_dict}
    min_weight = min(non_zero_weights)
    max_weight = max(non_zero_weights)
    if min_weight == max_weight:
        return {node: 1 if weight != 0 else 0 for node, weight in weights_dict.items()}
    return {node: (weight - min_weight) / (max_weight - min_weight) if weight != 0 else 0
            for node, weight in weights_dict.items()}

def calculate_distances(newick):
    tree = Phylo.read(StringIO(newick), "newick")
    terminals = tree.get_terminals()
    seq_names_full = [terminal.name for terminal in terminals if terminal.name.startswith('seq')]
    seq_names = [name.split('@')[0] for name in seq_names_full]
    distances = np.zeros((len(seq_names), len(seq_names)))
    
    for i, seq1 in enumerate(seq_names_full):
        for j, seq2 in enumerate(seq_names_full):
            if i != j:
                distances[i, j] = tree.distance(seq1, seq2)
    
    return seq_names, distances

def normalize_matrix(matrix):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    if min_val == max_val:
        return np.zeros_like(matrix)
    return (matrix - min_val) / (max_val - min_val)

def calculate_D(dist1, dist2, max_nodes):
    if dist1.shape[0] < max_nodes:
        dist1 = np.pad(dist1, ((0, max_nodes - dist1.shape[0]), (0, max_nodes - dist1.shape[1])))
    if dist2.shape[0] < max_nodes:
        dist2 = np.pad(dist2, ((0, max_nodes - dist2.shape[0]), (0, max_nodes - dist2.shape[1])))
    
    diff = dist1 - dist2
    diff_squared = np.power(diff, 2)
    sum_diff_squared = np.sum(diff_squared)
    root_sum_squared = np.sqrt(sum_diff_squared)
    return root_sum_squared / max_nodes

def calculate_penalty(tree1, tree2):
    common_nodes = np.sum(np.logical_and(tree1 != 0, tree2 != 0))
    total_nodes = np.sum(np.logical_or(tree1 != 0, tree2 != 0))
    return 1 - (common_nodes / total_nodes)

# Main script
input_path = os.path.expanduser("~/1.mahsa.farnia/3lineages.mathematical.representation/example.txt")
output_path = os.path.expanduser("~/1.mahsa.farnia/3lineages.mathematical.representation/output.txt")

with open(input_path, 'r') as f:
    lines = f.readlines()

all_weights = {}
all_distances = []
all_seq_names = []
tree_labels = []

for i, line in enumerate(lines, start=1):
    line = line.strip()
    if not line or ':' not in line:
        continue
    
    tree_label, newick = line.split(':', 1)
    tree_labels.append(f"Tree {i}")
    newick = newick.strip()
    
    weights = parse_newick(newick)
    for node, weight in weights.items():
        if node not in all_weights:
            all_weights[node] = [0] * (i - 1)
        all_weights[node].append(weight)
    
    for node in all_weights:
        if len(all_weights[node]) < i:
            all_weights[node].extend([0] * (i - len(all_weights[node])))
    
    try:
        seq_names, distances = calculate_distances(newick)
        normalized_distances = normalize_matrix(distances)  # Normalize the distances
        all_distances.append(normalized_distances)  # Store the normalized distances
        all_seq_names.append(seq_names)
    except ValueError as e:
        print(f"Error processing tree {tree_label}: {e}")
        continue

all_nodes = sorted(all_weights.keys())
original_weights_matrix = np.array([all_weights[node] for node in all_nodes])

nodes_per_tree = np.count_nonzero(original_weights_matrix, axis=0)

normalized_weights_matrix = np.zeros_like(original_weights_matrix)
for i, node in enumerate(all_nodes):
    normalized_weights = normalize_weights(dict(enumerate(all_weights[node])))
    normalized_weights_matrix[i] = [normalized_weights[j] for j in range(len(tree_labels))]

num_trees = len(tree_labels)
diff_columns = []
diff_labels = []
normalized_diff_sums = []

for i in range(num_trees):
    for j in range(i+1, num_trees):
        diff = np.abs(normalized_weights_matrix[:, i] - normalized_weights_matrix[:, j])
        diff_columns.append(diff)
        diff_labels.append(f"Diff {tree_labels[i]}-{tree_labels[j]}")
        
        max_nodes = max(nodes_per_tree[i], nodes_per_tree[j])
        normalized_sum = np.sum(diff) / max_nodes
        normalized_diff_sums.append(normalized_sum)

extended_normalized_matrix = np.hstack((normalized_weights_matrix, np.column_stack(diff_columns)))

column_sums = np.sum(extended_normalized_matrix, axis=0)

D_values = {}
P_values = {}
W_values = {}
GBLD_values = {}

for i in range(num_trees):
    for j in range(i+1, num_trees):
        max_nodes = max(nodes_per_tree[i], nodes_per_tree[j])
        D = calculate_D(all_distances[i], all_distances[j], max_nodes)
        D_values[(tree_labels[i], tree_labels[j])] = D
        
        P = calculate_penalty(original_weights_matrix[:, i], original_weights_matrix[:, j])
        P_values[(tree_labels[i], tree_labels[j])] = P
        
        W = normalized_diff_sums[len(W_values)]
        W_values[(tree_labels[i], tree_labels[j])] = W
        
        GBLD = P + W + D
        GBLD_values[(tree_labels[i], tree_labels[j])] = GBLD

# Save results
with open(output_path, 'w') as f:
    f.write("Original Weights:\n")
    f.write("Node," + ",".join(tree_labels) + "\n")
    for i, node in enumerate(all_nodes):
        f.write(f"{node}," + ",".join(f"{val:.4f}".rjust(10) for val in original_weights_matrix[i]) + "\n")
    
    f.write("\nNormalized Weights with Differences:\n")
    f.write("Node," + ",".join(tree_labels) + "," + ",".join(diff_labels) + "\n")
    for i, node in enumerate(all_nodes):
        f.write(f"{node}," + ",".join(f"{val:.4f}".rjust(10) for val in extended_normalized_matrix[i]) + "\n")
    
    f.write("Sum," + ",".join(f"{val:.4f}".rjust(10) for val in column_sums) + "\n")
    
    normalized_sums_row = ["-"] * num_trees + [f"{val:.4f}".rjust(10) for val in normalized_diff_sums]
    f.write("Normalized Sum," + ",".join(normalized_sums_row) + "\n")
    
    f.write("Nodes," + ",".join(f"{val}".rjust(10) for val in nodes_per_tree) + "\n")

    f.write("\nD_(T1,T2) Values:\n")
    for (tree1, tree2), D in D_values.items():
        f.write(f"D_({tree1},{tree2}) = {D:.4f}\n")

    f.write("\nP_(T1,T2) Values (Penalty):\n")
    for (tree1, tree2), P in P_values.items():
        f.write(f"P_({tree1},{tree2}) = {P:.4f}\n")

    f.write("\nW_(T1,T2) Values:\n")
    for (tree1, tree2), W in W_values.items():
        f.write(f"W_({tree1},{tree2}) = {W:.4f}\n")

    f.write("\nGBLD_(T1,T2) Values:\n")
    for (tree1, tree2), GBLD in GBLD_values.items():
        f.write(f"GBLD_({tree1},{tree2}) = {GBLD:.4f}\n")

    f.write("\nNormalized Distances:\n")
    for i, (distances, seq_names) in enumerate(zip(all_distances, all_seq_names)):
        tree_label = lines[i].split(':', 1)[0]
        f.write(f"{tree_label}: ,{',      '.join(seq_names)}\n")
        for j, row in enumerate(distances):
            f.write(f"{seq_names[j]}," + ",".join(f"{val:.4f}".rjust(10) for val in row) + "\n")
        f.write("\n")

print(f"Results saved to {output_path}")
 
