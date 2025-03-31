# An analysis of StarWars data using Python, dbt, and Quarto

This is a toy project fetching data from the [Star Wars API (SWAPI)](https://swapi.dev/), transforming the data into facts and dimensions model, and presenting some insights of the data in a Quarto-document.

## Running the code 
The project is divided into three different steps, each running separately. 

### Setup

Install the conda environment with 

```conda env create -f environment.yml``` 

### Step 1: Fetch data
First, in order to fetch the data, run 

```python python_code/source_data.py```

### Step 2: 
In order to run the dbt data pipeline, run

```dbt build```

### Step 3: ~~Profit~~ Analysis (not implemented yet)

A Quarto file with some simple analyses will be drafted shortly.