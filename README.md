# An analysis of StarWars data using Python, dbt, and Quarto

This is a toy project fetching data from the [Star Wars API (SWAPI)](https://swapi.dev/), transforming the data into facts and dimensions model, and presenting some insights of the data in a Quarto-document.

## Running the code 
The project is divided into three different steps, each running separately. 

### Setup

1. Clone this repository to your local machine

2. Install the conda environment with 
```conda env create -f environment.yml``` 

### Step 1: Fetch data
In order to fetch the data, run ```python python_code/source_data.py```. 

### Step 2: DBT
In order to run the dbt data pipeline, run ```dbt build``` after you've fetched the data.

### Step 3: Analysis

You can see the results of my analysis at [https://jtsuvile.github.io/starwars_analysis/](https://jtsuvile.github.io/starwars_analysis/) or by rendering the Quarto document on your own machine. 

To render the document locally:

1. Make sure you have Quarto installed locally ([see instructions here](https://quarto.org/docs/get-started/))
2. In a terminal window navigate to this repository and run ```quarto render``` to render [index.qmd](index.qmd)
3. The rendered document will appear at [docs/index.html](docs/index.html)