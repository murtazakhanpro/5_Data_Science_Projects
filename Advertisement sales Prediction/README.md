# Advertising Sales Prediction

Regression analysis of media spend and product sales

## Project overview

This project explores the supplied advertising dataset and compares linear regression with a random forest to predict sales from TV, radio, and newspaper budgets.

## Data

200 observations; predictors are TV, radio, and newspaper advertising budgets; target is sales. A fixed 80/20 train/test split and random_state 42 make the comparison reproducible.

## Workflow

Checked data types, missingness, descriptive statistics, pairwise relationships, individual spend-versus-sales patterns, and correlations. Trained a standardized linear regression baseline and a random forest regressor. Evaluated with MAE, RMSE, and R-squared, then checked held-out residuals.

## Results

On the held-out split, Random Forest achieved MAE 0.662, RMSE 0.791, and R-squared 0.980; linear regression achieved MAE 1.461, RMSE 1.782, and R-squared 0.899. In the standardized linear model, TV had the largest coefficient (3.764), followed by radio (2.792); newspaper was small (0.056). These are predictive associations, not causal channel effects.

## Limitations

This is a small, classic observational dataset. Results depend on the random split and may not generalize to another market, time period, or campaign. The coefficient ranking does not establish incremental causal returns.

## Run the notebook

Open advertising_sales_prediction.ipynb in Jupyter and run all cells. Keep Advertising Budget and Sales.csv in this folder.

## Project files

- `advertising_sales_prediction.ipynb` - executable analysis, visualizations, and results
- `Project_Documentation.pdf` - project summary with selected analysis visuals
- Source CSV files are noted above when the project uses local data.
