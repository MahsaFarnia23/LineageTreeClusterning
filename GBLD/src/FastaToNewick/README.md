# 🧬 FASTA to Newick Converter and Cleaner

### 📚 Description:
This script is designed to automate the process of converting a FASTA file to a Newick format tree, cleaning the Newick file, and integrating sequence counts into the Newick tree. It leverages the MUSCLE alignment tool for sequence alignment and constructs phylogenetic trees using the Neighbor-Joining (NJ) method.

### 🛠️ Requirements:
- 🖥️ **Operating System**: Linux/UNIX
- 🐍 **Python Libraries**:  
  - `Biopython` (for handling biological sequences and trees)
  - `subprocess` (for executing external commands)
  - `re` (for regular expressions)
- **MUSCLE** (Alignment Tool) should be installed and accessible in your system's PATH.

### ⚙️ Installation:

1. **Install Biopython**:
   You can install Biopython using `pip`:
   ```bash
   pip install biopython
   ```

2. **Install MUSCLE**:
   Download and install MUSCLE from [here](https://www.drive5.com/muscle/).

### 🏗️ How it Works:

The script performs the following steps:
1. **Convert FASTA to Newick Format**:
   - Aligns the sequences in the FASTA file using MUSCLE.
   - Constructs a phylogenetic tree using the Neighbor-Joining method.
   - Converts the tree into the Newick format.

2. **Clean the Newick File**:
   - Removes unnecessary labels like "Inner" and their associated numbers from the Newick file.

3. **Add Sequence Counts to Newick Tree**:
   - Updates the Newick tree with sequence counts extracted from the FASTA file.

### 🔧 Usage:

#### 1️⃣ Convert FASTA to Newick:
To convert a FASTA file to a Newick tree, run:
```python
fasta_to_newick(fasta_file, muscle_path, output_file)
```
Where:
- `fasta_file`: Path to the input FASTA file.
- `muscle_path`: Path to the MUSCLE alignment tool.
- `output_file`: Path to save the output Newick tree.

#### 2️⃣ Clean the Newick File:
The script cleans the Newick tree by removing labels such as "Inner" followed by a number.
```python
remove_inner(text)
```

#### 3️⃣ Add Sequence Counts to Newick Tree:
The Newick tree is updated with sequence counts from the FASTA file:
```python
update_newick_with_counts(newick_file, sequence_counts, output_file)
```

Where:
- `newick_file`: Path to the Newick tree file.
- `sequence_counts`: Dictionary of sequence IDs and counts.
- `output_file`: Path to save the updated Newick tree.

### 📝 Example:

```bash
python script.py
```

This will:
1. Align sequences using MUSCLE.
2. Construct the phylogenetic tree.
3. Clean the Newick tree.
4. Update the tree with sequence counts.

### 📁 File Structure:
```bash
|-- script.py              # Main script
|-- D3-N.fasta             # Input FASTA file
|-- D3-N_newick.txt        # Output Newick tree
|-- D3-N_newick_cleaned.txt # Cleaned Newick tree
|-- D3-N_sequence.txt      # Sequence counts file
|-- weighted_newick_D3-N.txt # Updated Newick tree with counts
```

### 🧑‍💻 Example Output:

- **Newick tree**:
  ```newick
  (seq1@182, seq2@110, (seq3@98, seq4@76));
  ```

- **Cleaned Newick tree**:
  ```newick
  (seq1, seq2, (seq3, seq4));
  ```

- **Sequence Counts**:
  ```
  >seq1@182
  >seq2@110
  >seq3@98
  >seq4@76
  ```

### 📧 Contact:
- **Mahsa Farnia**: [Mahsa.Farnia@USherbrooke.ca](mailto:Mahsa.Farnia@USherbrooke.ca)
- GitHub: [@MahsaFarnia](https://github.com/MahsaFarnia)
