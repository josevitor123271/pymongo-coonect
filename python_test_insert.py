# Import the pymongo_get_database.py file
from pymongo_get_database import get_database

# Get the database
db_name = get_database()

# Get the collection
collection_name = db_name["pacientes"]

# Paciente 1
paciente1 = {
    "_id": 111,
    "nome": "Juan",
    "idade": 30,
    "sexo": "M",
    "endereco": "Calle 123",
    "telefone": "1234567890"
}

paciente2 = {
    "_id": 222,
    "nome": "Maria",
    "idade": 25,
    "sexo": "F",
    "endereco": "Calle 456",
    "telefone": "0987654321"
}

# Insert the documents
collection_name.insert_many([paciente1, paciente2])

# Print the documents
pacientes = list(collection_name.find())
print(pacientes)