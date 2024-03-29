import logging
import unittest
import json
from microservice.interceptors.Impl.Sanitizer import Sanitizer
from pathlib import Path
import os

class TestSanitizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Deshabilitar la salida de registro antes de ejecutar las pruebas
        logging.disable(logging.CRITICAL)

    def test_data_sanitizer_workitems_valid_input(self):
        '''Caso de prueba para data_sanitizer_workitems con entrada válida'''
        
         #Arrage
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../resources/data_input.json")
        
        #Arrange
        with open(path) as file:
            input_workitems = json.load(file)
        
        #Act
        result = Sanitizer.data_sanitizer_workitems(input_workitems)
        data = json.loads(result)        
        workitems_count = len(data["workitems"])
        workitem_ids = [item["WorkItemId"] for item in data["workitems"]]
        workitem_type = set([item["WorkItemType"] for item in data["workitems"]])

        #Assert
        self.assertIsNotNone(data)
        self.assertEqual(workitems_count, 3)
        self.assertCountEqual(workitem_ids, ['14761-2024-02-08T13:52:52.277-06:00', '17413-2024-02-08T15:33:12.597-06:00', '17417-2024-02-08T16:15:04.237-06:00'])
        self.assertEqual(len(workitem_type), 1)
        
    def test_data_sanitizer_workitems_invalid_input(self):
        '''Caso de prueba para data_sanitizer_workitems con entrada no válida'''
        #Arrange
        input_workitems = {"invalid": "input"}

        #Act
        with self.assertRaises(ValueError) as error:
             Sanitizer.data_sanitizer_workitems(input_workitems)
        
        #Assert
        self.assertEqual(str(error.exception), "No se pudo validar el schema de workitems")

if __name__ == '__main__':
    unittest.main()
