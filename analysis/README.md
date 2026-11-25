# Verification script

The script `reproduce.py` uses only the Python standard library (Python 3.9+).

From repository root, run `python analysis/reproduce.py` **only after** the four original derived CSV files have been reviewed for sharing permission and placed in `data/` with these exact names:

- `corpus_status.csv`
- `candidate_status.csv`
- `cityspec_contrasts.csv`
- `grtp_contrasts.csv`

The CSVs are not present in the initial GitHub commit. The file `results/verification.json` is an independently generated local snapshot from the development archive, not a GitHub CI execution.

The script checks identifier cardinalities, historical record accounting, arithmetic of selected matched comparisons and one illustrative utility calculation. Passing does not authenticate source PDFs or resolve eligibility screening.
