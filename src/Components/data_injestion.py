import os
import sys

sys.path.append('C:\\Users\\yashw\\AI - Python - Self\\Krish_Naik\\ML Projects')
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
class DataInjestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataInjestion:
    def __init__(self):
        self.injestion_config=DataInjestionConfig()

    def initiate_data_injestion(self):
        logging.info('Entered data injestion method')
        try:
            df=pd.read_csv('C:\\Users\\yashw\\AI - Python - Self\\Krish_Naik\\ML Projects\\src\\Notebook\\data\\stud.csv')
            logging.info('read the dataset as a dataframe')

            os.makedirs(os.path.dirname(self.injestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.injestion_config.raw_data_path,index = False, header=True)
            logging.info('Train test split initiated')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path,index = False, header=True)

            test_set.to_csv(self.injestion_config.test_data_path,index = False, header=True)

            return(
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path,

    
            )

            logging.info('Injestion is complete')
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    print(f'sys_path --- {sys.path}')
    obj=DataInjestion()
    obj.initiate_data_injestion()
    print('file is complete')


