# COMP1013 Assignment 2.2 — Multimodal Product Type Classification

## Group
- Juin Hong Tong — a1845206
- Syed Tousif Mahadi Farabi — a1977855
- Spoorthi — a1956386

## Project
This project classifies Amazon Berkeley Objects (ABO) product types using catalogue images and English titles.

## Final models
- Text-only baseline
- Image-only baseline
- Feature fusion (ResNet-50 + DistilBERT embeddings + MLP)
- Late fusion (validation-tuned weighted probability fusion)

## Final data
- 10 balanced product types
- 2,500 products total
- Train: 1,750
- Validation: 375
- Test: 375
- Random seed: 42

## Final test results

| Model | Accuracy | Macro-F1 | Weighted-F1 |
|---|---:|---:|---:|
| Feature fusion | 0.904 | 0.903 | 0.904 |
| Image only | 0.861 | 0.858 | 0.859 |
| Late fusion | 0.861 | 0.858 | 0.858 |
| Text only | 0.813 | 0.814 | 0.815 |

Best late-fusion weights:
- Image: 0.6
- Text: 0.4

## Reproduce in Google Colab
1. Open `notebooks/COMP1013_Project_2_2_FINAL_COLAB.ipynb`.
2. Select a T4 GPU runtime.
3. Run all cells from top to bottom.
4. The notebook downloads the required ABO metadata/images automatically and exports result tables and figures.

## Repository structure
- `notebooks/` — final Colab notebook
- `src/` — small helper modules
- `results/` — final CSV/JSON metrics, models and figures from the completed run
- `report/` — final report DOCX and PDF
- `requirements.txt` — dependencies

## Dataset
Amazon Berkeley Objects (ABO):  
https://www.amazon.science/code-and-datasets/amazon-berkeley-objects-abo-dataset
