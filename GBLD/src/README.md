# Bioinformatics Tools Overview

![Bioinformatics](https://img.shields.io/badge/Field-Bioinformatics-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-brightgreen)

This repository contains a collection of Python scripts designed for bioinformatics and computational biology tasks, including sequence counting, phylogenetic tree analysis, lineage tree comparison, and clustering. Below is a brief overview of each tool's functionality and how to use them.

---

## 1. Nucleotide Sequence Counter

### Description:
A Python script that processes multiple TSV files in a specified directory to count the occurrences of each nucleotide sequence in the 'nucleotide' column.

### Key Features:
- Reads TSV files and counts nucleotide sequence occurrences. 🧬
- Outputs nucleotide counts to a text file. 📑

### Usage:
1. Set the directory containing the `.tsv` files. 📁
2. Run the script to process all TSV files and generate a count report. 📊

### Dependencies:
- `pandas` ![pandas](https://img.shields.io/badge/pandas-1.3.0-orange)  
- `os` 🖥️  
- `collections` 🔢

---

## 2. FASTA to Newick Converter and Cleaner

### Description:
This script automates the conversion of a FASTA file into a Newick format phylogenetic tree, aligns sequences using MUSCLE, and cleans the Newick tree by removing unnecessary labels. It also integrates sequence counts into the Newick tree.

### Key Features:
- Converts FASTA to Newick format. 🔄
- Aligns sequences using MUSCLE. ⚙️
- Cleans Newick files by removing inner node labels. ✂️
- Adds sequence counts to the Newick tree. 🧮

### Usage:
1. Convert FASTA to Newick format using MUSCLE. 🔬
2. Clean the Newick file and update it with sequence counts. 📈

### Dependencies:
- `Biopython` ![Biopython](https://img.shields.io/badge/Biopython-1.79-blue)  
- `subprocess` 🖱️  
- `re` 🔍  
- `MUSCLE` (alignment tool) ![MUSCLE](https://img.shields.io/badge/MUSCLE-Alignment-orange)  

---

## 3. Generalized Branch Length Distance (GBLD) Program

### Description:
The GBLD program computes a distance metric for comparing lineage trees in Newick format by considering branch lengths, tree structure, and overlapping nodes.

### Key Features:
- Parses Newick trees and extracts node weights. 🧬
- Computes pairwise differences in weights and branch lengths. 🔢
- Calculates the Generalized Branch Length Distance (GBLD) metric, including components for weight differences, structural distance, and penalties for overlapping nodes. ⚖️

### Usage:
1. Prepare input files containing Newick-formatted trees. 📂
2. Run the script to compute the GBLD metric for tree comparisons. 📏

### Dependencies:
- `Biopython` ![Biopython](https://img.shields.io/badge/Biopython-1.79-blue)

---

## 4. DBSCAN Clustering on Distance Matrix

### Description:
A Python script that applies DBSCAN clustering on a precomputed distance matrix to identify clusters and outliers.

### Key Features:
- Performs DBSCAN clustering based on a pairwise distance matrix. 📊
- Identifies clusters and labels outliers. 🚨
- Displays the cluster assignments for each data point. 📌

### Usage:
1. Provide a precomputed distance matrix. 🗂️
2. Run the script to perform clustering and display the results. 🖥️

### Dependencies:
- `numpy` ![numpy](https://img.shields.io/badge/numpy-1.21.2-blue)  
- `sklearn` ![sklearn](https://img.shields.io/badge/scikit-learn-0.24.2-yellow)  

---

## Installation

To run these scripts, ensure you have the following dependencies installed:

### 1. **Install Python Libraries**:  
For `Nucleotide Sequence Counter`:  
```bash
pip install pandas
```
For `FASTA to Newick Converter`:  
```bash
pip install biopython
```

For `DBSCAN Clustering`:  
```bash
pip install numpy scikit-learn
```

2. **MUSCLE** for the `FASTA to Newick Converter`:  
Download and install MUSCLE from [here](https://www.drive5.com/muscle/). 💻

---

## File Structure

```bash
|-- nucleotide_sequence_counter.py     # Nucleotide sequence counter script 🧬
|-- fasta_to_newick_converter.py       # FASTA to Newick conversion script 🔄
|-- gbld_program.py                    # GBLD program for lineage tree comparison ⚖️
|-- dbscan_clustering.py               # DBSCAN clustering script 📊
|-- *.tsv                              # Input TSV files for nucleotide counter 📑
|-- *.fasta                            # Input FASTA files for Newick converter 🔬
|-- distance_matrix.npy                # Precomputed distance matrix for DBSCAN 🗂️
```

---


