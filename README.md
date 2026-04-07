# PicoFold

A lightweight, CPU-only protein folding pipeline powered by ESMFold. PicoFold enables fast and efficient protein structure prediction without requiring GPU resources, making it accessible for researchers and developers with standard computing hardware.

## Features

- **CPU-Only Execution**: No GPU required - run protein folding on standard CPUs
- **ESMFold Integration**: Leverages Meta's ESMFold model for accurate protein structure predictions
- **Simple API**: Easy-to-use Python interface for protein sequence analysis
- **PDB Output**: Generates standard PDB format files for protein structures
- **Sequence Validation**: Built-in amino acid sequence validation and cleaning
- **Lightweight**: Minimal dependencies for easy installation and deployment

## What is Protein Folding?

Protein folding is the process by which amino acid chains fold into their native 3D structures. These structures are critical for understanding protein function, drug design, and disease research. ESMFold uses evolutionary sequence models to predict these structures from amino acid sequences alone.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/markxbrooks/PicoFold.git
   cd PicoFold
Install dependencies

bash
pip install -r requirements.txt
Or use pip-tools for better dependency management:

bash
pip install pip-tools
pip-sync requirements.txt
Dependencies
torch: Deep learning framework
torchvision: Vision utilities for PyTorch
torchaudio: Audio processing for PyTorch
fair-esm: Meta's ESMFold model
biopython: Bioinformatics toolkit
transformers: Pre-trained model library
Usage
Basic Example
Python
from main import run_esmfold

# Define your protein sequence (amino acids)
sequence = "MGSSHHHHHHSSGLVPRGSHM"

# Run the folding prediction
run_esmfold(sequence, output_pdb="my_protein.pdb")
Advanced Usage
Python
from main import run_esmfold, clean_sequence, validate_sequence

# Your protein sequence
sequence = "ACDEFGHIKLMNPQRSTVWY"

# Clean the sequence (removes invalid characters)
cleaned = clean_sequence(sequence)

# Validate the sequence
validate_sequence(cleaned)

# Run ESMFold
run_esmfold(cleaned, output_pdb="output.pdb")
Output
The pipeline generates a PDB file (Protein Data Bank format) containing:

Atomic coordinates of the predicted structure
Confidence scores per residue
Secondary structure information
View the output with molecular visualization tools like:

PyMOL
Chimera
Jmol
Online viewers (PyMOL web, 3Dmol.org)
API Reference
run_esmfold(sequence: str, output_pdb: str = "output.pdb")
Predicts protein structure from an amino acid sequence.

Parameters:

sequence (str): Amino acid sequence using standard single-letter codes
output_pdb (str): Path to save the output PDB file (default: "output.pdb")
Returns: None (writes PDB file to disk)

clean_sequence(seq: str) -> str
Cleans invalid amino acids from a sequence by replacing them with Alanine (A).

Parameters:

seq (str): Input amino acid sequence
Returns: Cleaned sequence string

validate_sequence(seq: str)
Validates that a sequence contains only valid amino acids.

Parameters:

seq (str): Amino acid sequence to validate
Raises: ValueError if invalid amino acids are found

Supported Amino Acids
PicoFold supports all 20 standard amino acids:

Letter	Amino Acid	Letter	Amino Acid
A	Alanine	N	Asparagine
C	Cysteine	P	Proline
D	Aspartic acid	Q	Glutamine
E	Glutamic acid	R	Arginine
F	Phenylalanine	S	Serine
G	Glycine	T	Threonine
H	Histidine	V	Valine
I	Isoleucine	W	Tryptophan
K	Lysine	Y	Tyrosine
L	Leucine		
M	Methionine		
Performance Notes
ESMFold is faster than AlphaFold2 while maintaining competitive accuracy
CPU-only inference is slower than GPU-accelerated prediction but requires no specialized hardware
Typical folding time depends on sequence length and system specifications
For production use with many sequences, consider GPU acceleration (modify device selection in main.py)
Project Structure
Code
PicoFold/
├── main.py                 # Core protein folding module
├── requirements.in         # High-level dependencies
├── requirements.txt        # Pinned dependency versions
├── output.pdb             # Example output file
├── README.md              # This file
└── LICENSE                # MIT License
License
This project is licensed under the MIT License - see the LICENSE file for details.

References
ESMFold Paper
Hugging Face Transformers
PyTorch Documentation
BioPython
Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

Acknowledgments
Meta AI for the ESMFold model
Hugging Face for the transformers library
PyTorch team for the deep learning framework