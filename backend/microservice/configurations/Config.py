from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_URL = os.getenv('API_URL')
    ELK_HOST = os.getenv('ELK_HOST')
    ELK_USER = os.getenv('ELK_USER')
    ELK_PWD = os.getenv('ELK_PWD')
    ELK_INDEX= os.getenv('ELK_INDEX')
    API_AZURE_PROJECTS= os.getenv('API_AZURE_PROJECTS')
    API_AZURE_TOKEN= os.getenv('API_AZURE_TOKEN')
    API_AZURE_WORKITEMS = os.getenv('API_AZURE_WORKITEMS')
    