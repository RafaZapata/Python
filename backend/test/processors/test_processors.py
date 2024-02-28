import unittest
import json
from microservice.processors.Impl.Data_processor import DataProcessor
from pathlib import Path
import os

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        # Configuración común para las pruebas
        self.data_processor = DataProcessor()

    def test_process_data(self):
        '''Caso de prueba para process_data con exito'''
        #Arrange

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../resources/data_sanitizer.json")

        with open(path, 'r') as file:
            data_input = json.load(file)
        
        data = json.dumps(data_input)

        #Act
        result = self.data_processor.process_data(data)
        result_dict = json.loads(result)
        workitems_count = len(result_dict)

        #Assert
        self.assertEqual(workitems_count, 3)
        self.assertIn('WorkItemId', result_dict[0])
        self.assertIn('WorkItemType', result_dict[0])
        self.assertIn('StoryPoint', result_dict[0])
        self.assertIn('Iteration', result_dict[0])
        self.assertIn('Project', result_dict[0])
        self.assertIn('AssignedTo', result_dict[0])
        self.assertIn('WorkItemId', result_dict[1])
        self.assertIn('WorkItemType', result_dict[1])
        self.assertIn('StoryPoint', result_dict[1])
        self.assertIn('Iteration', result_dict[1])
        self.assertIn('Project', result_dict[1])
        self.assertIn('AssignedTo', result_dict[1])
        self.assertIn('WorkItemId', result_dict[2])
        self.assertIn('WorkItemType', result_dict[2])
        self.assertIn('StoryPoint', result_dict[2])
        self.assertIn('Iteration', result_dict[2])
        self.assertIn('Project', result_dict[2])
        self.assertIn('AssignedTo', result_dict[2])

if __name__ == '__main__':
    unittest.main()
