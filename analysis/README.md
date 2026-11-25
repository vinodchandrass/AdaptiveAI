# Verification script

The script `reproduce.py` uses only the Python standard library (Python 3.9+).

From repository root, run `python analysis/reproduce.py` **only after** the four original derived CSV files have been reviewed for sharing permission and placed in `data/` with these exact names:

- `corpus_status.csv`
- `candidate_status.csv`
- `cityspec_contrasts.csv`
- `grtp_contrasts.csv`

The four CSVs are now present in the private repository. Remote contents were checked on 2026-11-25 using equivalent identifier and arithmetic checks; this is not a Python CI run. The file `results/verification.json` is an independently generated local snapshot from the development archive, not a GitHub CI execution.

The script checks identifier cardinalities, historical record accounting, arithmetic of selected matched comparisons and one illustrative utility calculation. Passing does not authenticate source PDFs or resolve eligibility screening.
