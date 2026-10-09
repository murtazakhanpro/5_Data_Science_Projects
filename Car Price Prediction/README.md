# Used Car Price Prediction

Data preparation and regression baselines for used-car listings

## Project overview

This project examines the supplied used-car dataset and builds two regression baselines using vehicle attributes such as brand, year, engine size, fuel type, transmission, mileage, condition, and model.

## Data

2,500 records and 10 source columns. The workflow normalizes category text, removes duplicates, converts numeric fields, creates car age relative to the current year, and excludes invalid prices and implausible ages.

## Workflow

Explored price distribution, price by fuel type, price versus age, and numeric correlations. Used a train/test split, median imputation and scaling for numeric fields, most-frequent imputation and one-hot encoding for categorical fields. Compared Ridge Regression and Random Forest with MAE, RMSE, and R-squared.

## Results

Ridge Regression was the better of the two tested models on the held-out split, with MAE 23,873.875, RMSE 27,788.760, and R-squared -0.019. The random forest had MAE 24,296.377, RMSE 28,208.886, and R-squared -0.050. Negative R-squared means neither baseline beat predicting the test-set mean on this split; this is an honest baseline, not a reliable pricing solution.

## Limitations

The supplied synthetic-looking data show weak learnable signal for these features and this split. Better sourced listings, currency/market context, and validation of price quality are needed before using the model for pricing decisions.

## Run the notebook

Open used_car_price_prediction.ipynb in Jupyter and run all cells. Keep car_price_prediction_.csv in this folder.

## Project files

- `used_car_price_prediction.ipynb` - executable analysis, visualizations, and results
- `Project_Documentation.pdf` - project summary with selected analysis visuals
- Source CSV files are noted above when the project uses local data.
