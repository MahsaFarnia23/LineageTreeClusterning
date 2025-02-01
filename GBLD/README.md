## 👨‍💻 Authors: Mahsa Farnia, Tahiris Lab  

# Immune System Lineage Tree Clustering using GBLD Metric

This repository contains the code for clustering human immune system lineage trees based on their similarities using the **Generalized Branch Length Distance (GBLD)** metric. The primary goal of this project is to evaluate the lineage trees of the human immune system and group them using **DBSCAN clustering**, leveraging a set of indices based on tree properties.

🌿 **Bioinformatics Project**  

## Overview

The **GBLD metric** is used in this project to evaluate the similarity between lineage trees of the human immune system. We focus on three primary indices:

1. **Penalty** based on the rate of uncommon nodes between two lineage trees. 
2. **Weight differences** between nodes in two lineage trees. 
3. **Branch length distance** between pairs of nodes. 

These indices are used to compute the pairwise distances between lineage trees, which are then clustered using the **DBSCAN algorithm**. 🧑‍💻

## Input Format

- **FASTA Format**: The lineage tree data is provided in **FASTA format**. 📄
- **Weighted Newick Trees**: The trees are converted into **weighted Newick format** to capture the necessary information for distance calculations. 🌳

## Methodology

1. **Data Input**: Lineage trees are read from FASTA files and converted into weighted Newick format. 📥
2. **Distance Calculation**: The **GBLD metric** is used to calculate the distance between lineage trees based on the penalty, weight differences, and branch length distance indices. 📏
3. **Clustering**: The pairwise distances are input into the **DBSCAN algorithm** for clustering the lineage trees based on their similarities. 🧑‍💻
4. **Evaluation**: The performance and effectiveness of the clustering approach are evaluated based on the indices and clustering results. 📊

## Key Features

- **FASTA to Newick Conversion**: Automated conversion of FASTA sequences into weighted Newick format. 🔄
- **Distance Indices**: Evaluation of lineage trees using penalty, weight differences, and branch length distances. 📐
- **Clustering with DBSCAN**: **DBSCAN** algorithm applied to group the lineage trees into clusters. 🔍
- **Scalability**: Can handle large datasets of immune system lineage trees for clustering and analysis. 📈

## Citation

If you use this project or the methodology in your research, please cite our paper:

> [GBLD Metric for Lineage Tree Clustering](https://link.springer.com/content/pdf/10.1186/s13015-024-00267-1.pdf) 📝

3. **View Results**: The clustered trees will be saved in the output directory, along with evaluation metrics. 🗂️

## Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, create an issue, or submit a pull request. 🤝

### 📧 Contact:
- **Mahsa Farnia**: [Mahsa.Farnia@USherbrooke.ca](mailto:Mahsa.Farnia@USherbrooke.ca)
- **Nadia Tahiri**: [Nadia.Tahiri@USherbrooke.ca](mailto:Nadia.Tahiri@USherbrooke.ca)
- GitHub: [@MahsaFarnia](https://github.com/MahsaFarnia)

