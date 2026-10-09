# Iris Flower Classification

Exploratory analysis and species model comparison

## Project overview

This project classifies iris flowers into Setosa, Versicolor, and Virginica from sepal and petal measurements using scikit-learn data built into Python.

## Data

150 observations, four numeric measurements, and three balanced species classes. No external dataset download is needed.

## Workflow

Reviewed shape, data types, missingness, descriptive statistics, species counts, pairwise feature plots, boxplots, and feature correlations. Compared standardized Logistic Regression and K-Nearest Neighbours on a stratified 80/20 split. Used five-fold cross-validation on the training partition as a stability check.

## Results

Both tested models reached 0.933 held-out accuracy. Both had mean training-fold cross-validation accuracy of 0.958 (SD 0.026). Logistic Regression is listed first as the tied model selected by the notebook. Petal length and petal width show the clearest species separation in the plots; sepal measurements overlap more.

## Limitations

Only 30 flowers are in the holdout set, so one classification changes accuracy by about 3.3 percentage points. This clean benchmark does not represent measurement noise or deployment conditions.

## Run the notebook

Open iris-flower-prediction-mlnotebook.ipynb in Jupyter and run all cells. The dataset loads from scikit-learn.

## Project files

- `iris-flower-prediction-mlnotebook.ipynb` - executable analysis, visualizations, and results
- `Project_Documentation.pdf` - project summary with selected analysis visuals
- Source CSV files are noted above when the project uses local data.
