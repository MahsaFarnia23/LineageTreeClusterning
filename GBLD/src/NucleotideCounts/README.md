# 📊 Nucleotide Sequence Counter

### 📚 Description:
This Python script processes multiple TSV (Tab-Separated Values) files in a specified directory to count the occurrences of each nucleotide sequence. It reads the nucleotide sequences from the 'nucleotide' column in the TSV files, aggregates the counts, and writes the results to a text file.

### 🛠️ Requirements:
- 🐍 **Python Libraries**:  
  - `pandas` (for handling and processing TSV files)
  - `os` (for interacting with the file system)
  - `collections` (for managing nucleotide counts)
  
To install `pandas`, you can use:
```bash
pip install pandas
```

### ⚙️ How It Works:
1. **Reads TSV files**: The script processes all `.tsv` files in the specified directory.
2. **Counts Nucleotide Sequences**: For each file, the script looks for the 'nucleotide' column and counts the occurrences of each nucleotide sequence.
3. **Saves Counts**: After processing all files, it writes the nucleotide counts to an output text file.

### 🔧 Usage:

#### 1️⃣ Define the Directory:
Set the path to the directory containing your `.tsv` files:
```python
directory_path = r'C:\path\to\your\tsv\files'
```

#### 2️⃣ Run the Script:
Simply execute the script. It will process all `.tsv` files in the specified directory and save the nucleotide counts to a file.

### 📝 Example:

```bash
python script.py
```

This will:
- Iterate over all `.tsv` files in the given directory.
- Count the occurrences of each nucleotide sequence in the 'nucleotide' column.
- Save the results to a text file named `1.nucleotide_counts.txt`.

### 📁 File Structure:
```bash
|-- script.py                # Main script
|-- *.tsv                    # Input TSV files containing nucleotide sequences
|-- 1.nucleotide_counts.txt  # Output file with nucleotide counts
```

### 🧑‍💻 Example Output:

The output file `1.nucleotide_counts.txt` will have the following format:
```
ATGC: 15
CGTA: 20
GCTA: 10
...
```

Where each line represents a nucleotide sequence and its corresponding count.

