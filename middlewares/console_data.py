from functools import wraps
from flask import request

def console_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Lógica antes de la función (middleware)
        print(f"Solicitando: {request.method} {request.path} {request.data}")
        
        # Llamar la función original
        return function(*args, **kwargs)
    
    return wrapper
