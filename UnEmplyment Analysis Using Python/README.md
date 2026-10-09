# Unemployment Trends in India

Regional and monthly analysis with a descriptive COVID-era comparison

## Project overview

This project explores regional and temporal patterns in India unemployment survey estimates using the supplied area-level CSV.

## Data

The primary area-level file contains 768 rows before cleaning and 740 after date parsing, missing-key removal, and duplicate removal. The observed date range is May 2019 to June 2020. A second state-level CSV is not pooled because it has a different grain.

## Workflow

Converted date and numeric fields; inspected shape, types, missingness, and descriptive statistics; calculated regional averages; plotted monthly trends, three well-covered state trajectories, and the top ten regional averages; and examined correlations among unemployment, employment, and labour participation estimates. Compared periods before March 2020 and from March 2020 onward.

## Results

The area-weighted mean unemployment estimate was 9.51% before March 2020 and 17.77% from March 2020 onward in this dataset. Tripura had the highest observed region-level mean (28.35%). The post-onset rise is descriptive and cannot isolate a pandemic effect from seasonality, other events, or survey measurement.

## Limitations

The available period is short and ends in June 2020. Area observations are equally weighted in regional averages, and the pre/post windows differ in length. The comparison is not causal evidence.

## Run the notebook

Open unemployment_india_eda.ipynb in Jupyter and run all cells. Keep Unemployment in India.csv in this folder.

## Project files

- `unemployment_india_eda.ipynb` - executable analysis, visualizations, and results
- `Project_Documentation.pdf` - project summary with selected analysis visuals
- Source CSV files are noted above when the project uses local data.
