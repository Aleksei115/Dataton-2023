# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import DashboardItem
from pymongo import MongoClient
import json
import pandas as pd
from datetime import datetime
from bson.json_util import dumps

# Create your views here.


def get_dashboard_data(request):
    # hostname = "mongodb+srv://datatondb.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
    # port = 27017  # Default MongoDB port
    # username = "alexgrim"  # If authentication is required
    # password = "cpcfi612_"  # If authentication is required

    # # Create a MongoClient instance
    # client = MongoClient(hostname, port, username=username, password=password)

    # db = client["dataton"]

    # collection = db["s1_EDOMEX"]

    # # Obtener todos los documentos
    # documentos = collection.find()

    # # cantidad de documentos
    # print("Cantidad de documentos: ", collection.count_documents({}))

    # # Imprimir el valor de la escolaridad
    # escolaridad = {}
    # maestria = 0
    # doctorado = 0
    # licenciatura = 0
    # especialidad = 0
    # bachillerato = 0
    # primaria = 0
    # secundaria = 0
    # tecnico = 0
    # for doc in documentos:
    #     i = 0
    #     while True:
    #         try:
    #             escolaridad_data = doc["declaracion"]["situacionPatrimonial"][
    #                 "datosCurricularesDeclarante"
    #             ]["escolaridad"][i]
    #             if "nivel" in escolaridad_data:
    #                 nivel_educativo = escolaridad_data["nivel"]["valor"]
    #                 escolaridad[i] = nivel_educativo
    #                 if nivel_educativo == "MAESTRÍA":
    #                     maestria += 1
    #                 elif nivel_educativo == "DOCTORADO":
    #                     doctorado += 1
    #                 elif nivel_educativo == "LICENCIATURA":
    #                     licenciatura += 1
    #                 elif nivel_educativo == "ESPECIALIDAD":
    #                     especialidad += 1
    #                 elif nivel_educativo == "BACHILLERATO":
    #                     bachillerato += 1
    #                 elif nivel_educativo == "PRIMARIA":
    #                     primaria += 1
    #                 elif nivel_educativo == "SECUNDARIA":
    #                     secundaria += 1
    #                 elif nivel_educativo == "CARRERA TÉCNICA O COMERCIAL":
    #                     tecnico += 1
    #             i += 1
    #         except IndexError:
    #             break
    #     print(escolaridad)

    # {
    #     "maestria": 13111,
    #     "doctorado": 6004,
    #     "licenciatura": 38852,
    #     "especialidad": 3224,
    #     "bachillerato": 14405,
    #     "primaria": 6813,
    #     "secundaria": 10627,
    #     "tecnico": 6558,
    # }

    # return all the data in the database
    print("Hello world")
    return JsonResponse(
        {
            "primaria": 6813,
            "secundaria": 10627,
            "bachillerato": 14405,
            "tecnico": 6558,
            "licenciatura": 38852,
            "especialidad": 3224,
            "maestria": 13111,
            "doctorado": 6004,
        }
    )
    

