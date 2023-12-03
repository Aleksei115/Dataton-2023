from pymongo import MongoClient
import json
import pandas as pd
from datetime import datetime
# Provide the connection details
hostname = 'mongodb+srv://datatondb.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'
port = 27017  # Default MongoDB port
username = 'alexgrim'  # If authentication is required
password = 'cpcfi612_'  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)

db = client['dataton']

collection = db['s1_EDOMEX']

# Obtener todos los documentos
documentos = collection.find()

# cantidad de documentos
print("Cantidad de documentos: ", collection.count_documents({}))

# Imprimir los primeros 5 documentos
for i, doc in enumerate(documentos):
    if i > 4:
        break
    print(doc)