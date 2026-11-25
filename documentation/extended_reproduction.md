# Extended reproducibility snapshot
Run `python analysis/reproduce.py` and `python analysis/reproduce_extended.py` from the repository root. For figures install matplotlib and run `python analysis/generate_figures.py`. Figures reproduce numerical content, not the exact manuscript layout.

`evidence_indicators.csv` is a projection of the existing 263 original-PDF page-anchored protocol evidence and full-text experimental evidence matrix, joined by WoS ID. The five core flags indicate positive page counts; numerical and control flags derive from positive candidate passage counts. These are machine-assisted indicators, not independently verified evidence or final eligibility. No excerpts or PDFs are included.

`table5_transcriptions.csv` transcribes prior source-linked assessment reports (Batch04 direct table verification, new original table effects, new matched retention evidence, MetacAdapt original source statistical correction). It does not independently re-extract values from original PDFs. CitySpec F1 means derive from existing paired rows. All effects are descriptive within-study contrasts. TRAF dispersion values are not reproduced by this extension. No pooled estimate is computed.

Original search execution, independent reviewer provenance, final eligibility and formal appraisal remain unresolved. Public redistribution requires separate approval.
