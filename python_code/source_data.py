import pandas as pd
import requests
import configparser
import pathlib
import warnings
import logging
logging.basicConfig(level=logging.INFO)


def make_request(query):
    """Get response to a request"""
    response = requests.get(query, verify=False)
    # TODO: could have more robust error handling for API calls, e.g. retries
    response.raise_for_status()
    return response.json()


def fetch_resource(query):
    """Fetch a response and convert to pandas dataframe"""

    # TODO: If this was a function I would use more broadly,
    # I would probably make flags to control
    # which variables get returned.
    resources = make_request(query)
    df = pd.json_normalize(resources['results'])
    next_page = resources['next']
    n_resources = resources['count']
    return df, next_page, n_resources


def get_all_of(url, resource_type):
    """ Get all resources of one type in the least number of API calls
    ie import data by page, not by element"""

    df, next_page, n_resources = fetch_resource(url+resource_type)
    counter = 1
    # loop over all pages of a single type of resource
    while next_page:
        df_page, next_page, _ = fetch_resource(next_page)
        df = pd.concat([df, df_page])
        counter += 1

    logging.info(f"Fetched {len(df)} rows of {resource_type} using {counter}" +
                 " calls to the SWapi")

    # Check if we got all resources we expected
    # I'm not 100% sure if this should be an error instead of a warning.
    # technically it does not break things but it might indicate a fundamental
    # data quality issue
    if (len(df) != n_resources):
        warnings.warn("""API reports %i instances of the requested resource
                      but API calls returned %i instances.
                      These values should match.""" % (n_resources, len(df)))

    return df


def main():
    """main logic of the script"""
    logging.info('Running data import as script')

    # get configuration from a config file
    config = configparser.ConfigParser()
    config.read(pathlib.Path(__file__).parent / "config.ini")
    url = config.get('general', 'url')
    relevant_tables = config.items("tables")

    # read in each table as defined in the config file
    # and save them as seeds for dbt to process
    for key, table in relevant_tables:
        resource_type = key
        df = get_all_of(url, resource_type)
        # Removing thousands indicator for a specific column in a specific
        # table since it's throwing errors that prevent the table from getting
        # loaded downstream
        # TODO: more robust quality control for the different columns
        if resource_type == 'starships':
            df['length'] = df['length'].str.replace(',', '')
        df.to_csv(pathlib.Path(__file__).parent.parent / 'seeds' /
                  f'raw_{resource_type}.csv')

    logging.info('Done with importing the following tables:' +
                 f'{", ".join(str(i[0]) for i in relevant_tables)}')


if __name__ == "__main__":
    main()
