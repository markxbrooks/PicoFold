from transformers import AutoTokenizer, EsmForProteinFolding
import torch

def run_esmfold(sequence: str, output_pdb: str = "output.pdb"):
    model_name = "facebook/esmfold_v1"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = EsmForProteinFolding.from_pretrained(model_name)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()
    sequence = clean_sequence(sequence)
    inputs = tokenizer(sequence, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    pdb = model.output_to_pdb(outputs)[0]

    with open(output_pdb, "w") as f:
        f.write(pdb)

    print(f"PDB saved to: {output_pdb}")


def validate_sequence(seq: str):
    valid = set("ACDEFGHIKLMNPQRSTVWY")
    if not set(seq).issubset(valid):
        raise ValueError("Invalid amino acid sequence")

def clean_sequence(seq: str) -> str:
    valid = set("ACDEFGHIKLMNPQRSTVWY")
    return "".join([c if c in valid else "A" for c in seq])

if __name__ == "__main__":
    sequence = "MGSSHHHHHHSSGLVPRGSHM"  # your protein sequence
    sequence = clean_sequence(sequence)
    run_esmfold(sequence)
