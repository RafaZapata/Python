from interceptors.ISanitizer import ISanitizer
from models.Azure_input_workitem_data_model import AzureInputWorkitemDM
import json
import logging

class Sanitizer(ISanitizer):

    def data_sanitizer_workitems(json_workitems):
        is_valid_schema = AzureInputWorkitemDM.validate_schema(json_workitems)
        if not is_valid_schema:
            logging.error("Error al validar el schema workitem")
            raise ValueError("No se pudo validar el schema de workitems")
        
        model_workitem = AzureInputWorkitemDM(json_workitems)

        return json.dumps(model_workitem.to_dict())