from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    # Iterate through each table in the dictionary
    for table_name, df in data.items():
        table_id = f'my-test-project-472309.uber_data_engineering_yt.{table_name}'
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            table_id,
            if_exists='replace',
        )
