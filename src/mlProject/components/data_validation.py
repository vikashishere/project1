import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig



class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n")
                        f.write(f"Column in data.csv: {all_cols}\n")
                        f.write(f"Column in schema: {all_schema}\n")
                        f.write(f"{col} is not present in {all_schema}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e