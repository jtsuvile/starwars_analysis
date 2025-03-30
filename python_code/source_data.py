import pandas as pd
import requests
import configparser
import pathlib


def make_request(query):
    # get response to a request 
    response = requests.get(query).json()
    # TODO: handle non-successful requests
    return response


def fetch_resource(query):
    # Fetch a response and convert to pandas dataframe

    # If this was a function we would use more broadly, 
    # I would probably make flags to control
    # which variables get returned.
    resources = make_request(query)
    df = pd.json_normalize(resources['results'])
    next_page = resources['next']
    n_resources = resources['count']
    return df, next_page, n_resources


def get_all_of(url, resource_type):
    # get all resources of one type in the least number of API calls
    # ie import data by page, not by element

    df, next_page, n_resources = fetch_resource(url+resource_type)
    counter = 1
    # loop over all pages of a single type of resource
    while next_page:
        df_page, next_page, _ = fetch_resource(next_page)
        df = pd.concat([df, df_page])
        counter += 1

    # check if we got all resources we expected
    if(len(df) == n_resources):
        print(f"Fetched all {n_resources} rows of {resource_type} using {counter} calls to the SWapi")
        return df
    else:
        # TODO: add some kind of simple exception handling
        print("no this was not good, we should throw an exception here")


if __name__ == "__main__":
    # main logic of the script
    print('Running data import as script')

    # get configuration from a config file
    config = configparser.ConfigParser()
    config.read(pathlib.Path(__file__).parent / "config.ini")
    url = config.get('general','url')
    relevant_tables = config.items( "tables" )

    # read in each table as defined in the config file 
    # and save them as seeds to dbt process
    for key, table in relevant_tables:
        print(key)
        print(table)
        resource_type = key
        df = get_all_of(url, resource_type)
        # TODO: consider separator character for csv, comma probably a bad choice
        df.to_csv(pathlib.Path(__file__).parent.parent / 'seeds' / f'raw_{resource_type}.csv')
    
    print('Done')

