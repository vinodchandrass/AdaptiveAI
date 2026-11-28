# Beyond Adaptation Accuracy

**A Systematic Review of Evidence Quality, Net Benefit, and Capability Preservation in Open-World AI**

This is the private development repository for the AdaptiveAI review, targeting ACM Computing Surveys. The original Web of Science corpus is fixed at **1,379 records**.

**Status: pre-release, not a completed systematic review or archived dataset.** Historical selection records contain 975 advanced records and 404 not advanced; 263 candidates in the current worklist remain **pending independently verified full-text eligibility**. These counts do not represent final included or excluded studies.

The preliminary, source-linked comparisons and mathematical framework are development materials. They do not establish corpus-wide results, finalized reviewer agreement, or independently validated net benefit.

## Reproducibility materials

- `protocol/`: documented research questions, eligibility framework and extraction criteria.
- `data/`: status tables and selected derived comparisons, subject to validation and licensing.
- `analysis/`: arithmetic and identifier verification.
- `documentation/release_gate.md`: outstanding source, licensing, and methodological verification requirements.

The reproducibility checks concern arithmetic and identifier linkage only. They **do not** reproduce the WoS search, original experiments, source authentication, independent review, or final PRISMA adjudication.

No copyrighted article PDFs, unrestricted original WoS exports, or reviewers' personal information should be committed. Do not issue a public release or Zenodo DOI until the release gate is resolved. No license is assigned pending author approval.

## Research title

Beyond Adaptation Accuracy: A Systematic Review of Evidence Quality, Net Benefit, and Capability Preservation in Open-World AI.

## Run the computational checks

Use Python 3.11 from the repository root:

```sh
python -m pip install -r requirements.txt
python analysis/reproduce.py
python analysis/reproduce_extended.py
python analysis/generate_figures.py
python analysis/run_all.py
```

The extended script checks all eight evidence-coverage counts, candidate linkage and CitySpec F1 means; it calculates differences from prior Table 5 transcriptions. The figure script regenerates numerical illustrations at 600 DPI, not necessarily identical graphical layouts. GitHub Actions runs these commands and checks that tracked JSON results are unchanged. Figure existence is checked, not pixel identity. A passing run does not authenticate original sources or establish final eligibility. Direct dependency version is pinned; transitive dependencies are not locked.

The standard-library regression suite checks six analytical cases, including 5,151 preference-weight combinations, Pareto frontiers, constraints, effect calculations and invalid weights. All six tests passed in author-side execution (28 November 2026). This establishes computational consistency, not independent empirical framework validation.
