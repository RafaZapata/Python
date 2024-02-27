import pandas as pd
import json
from processors.IData_processor import IDataProcessor

class DataProcessor(IDataProcessor):
    def process_data(self, data_input):
        
        dt = json.loads(data_input)
        df = pd.DataFrame(dt['workitems'])
        df.columns = ['' + col for col in df.columns]
        json_resultado = df.to_json(orient='records', indent=4)

        return json_resultado