# SK hynix DART Financial Analysis

GitHub repository: https://github.com/oosudz02-creator/sk-hynix

## Source / scope
- DART annual report for FY2025, filed 2026-03-17, SK hynix Inc.
- Consolidated IFRS figures; monetary values are KRW million.
- Extracted comparison periods: FY2023–FY2025.
- Reference guide supplied by user informs ratio definitions and analysis sequence.

## Data notes
`data/consolidated_financials_krw_million.csv` contains report-derived inputs and formula-derived metrics.
`data/financial_ratios.csv` contains key ratio outputs.
Cash-only net debt = interest-bearing borrowings (current + non-current) less cash and cash equivalents. Short-term financial products are not deducted.
CAPEX = cash purchases of property, plant and equipment plus intangible assets. FCF = CFO - this CAPEX definition.
CFO/net income is not meaningful when net income is negative; interpret accordingly.
ROA/ROE use average opening/closing assets/equity and are only populated for FY2024–FY2025 because FY2022 opening balances are not included.
Interest coverage omitted pending extraction of interest expense specifically; do not substitute total finance costs.
2025 report statements are subject to shareholder approval as stated in the filing.

## Reproduce
```bash
python -m pip install -r requirements.txt
python analyze.py
```

## Publish to the configured GitHub repository
From a local clone of the repository, copy this project folder contents into the repository root, then run:
```bash
git add README.md analyze.py requirements.txt data/
git commit -m "Add SK hynix FY2023-FY2025 financial analysis"
git push origin main
```
If you have not cloned it yet:
```bash
git clone https://github.com/oosudz02-creator/sk-hynix.git
```

## Source file handling
Commit the original PDF and XBRL ZIP under `source/` only if redistribution is permitted; otherwise retain them locally and commit the extracted data, extraction script, and source metadata. Add DART filing URL / filing date and record any manual corrections.
