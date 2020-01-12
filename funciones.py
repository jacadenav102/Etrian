import re


def crea_respusta_patrones(diccionario_patrones:dict,texto:str):
    """
    Regresa la respuesta adecuada para un texto a partir de un diccionario que tenga almacenada esta información.\n
    PARAMETROS:\n
    diccionario_patrones (dict): Diccionario donde las llaves son los patrones a buscar y su contenido
    las respuesta al patrón.\n
    text (str): Texto donde se buscará el patrón.\n
    escepcion (str): Nombre de la llave que tiene la respuesta en caso de no encontrarse un patrón.\n
    RETORNA:\n
    object : Puede ser una lista o un texto, este es el contenido del diccionario.
    """
        
    for pregunta,respuesta  in diccionario_patrones.items():
        if re.search(pregunta,texto):
            return respuesta

            

        
