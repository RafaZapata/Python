import logging
import unittest
import json
from microservice.interceptors.Impl.Sanitizer import Sanitizer

class TestSanitizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Deshabilitar la salida de registro antes de ejecutar las pruebas
        logging.disable(logging.CRITICAL)

    def test_data_sanitizer_workitems_valid_input(self):
        '''Caso de prueba para data_sanitizer_workitems con entrada válida'''
        #Arrange
        with open('..\\backend\\tests\\resources\\data_input.json', 'r') as file:
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
        self.assertCountEqual(workitem_ids, [14761, 17413, 17417])
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
