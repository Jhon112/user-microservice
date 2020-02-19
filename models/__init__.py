import os
from models.base_model import BaseModel
from models.user import User

"""CLASSES - dictionary = { Class Name (string) : Class Type }"""

from models.engine import db_storage
CLASSES = db_storage.DBStorage.CLASSES
storage = db_storage.DBStorage()
storage.reload()
