#Purpose: Serializes MongoDB documents into Python dictionaries.

#Converts a MongoDB document to a dictionary.
#finding key to reutrn the value (ie _id is for that)
#convert the id object typ ei a strnig

def individual_serial(todo) -> dict:
    
    #_id used for findind the key to return the value

    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "desc": todo["desc"],
        "comp": todo["comp"]  
        }
#deserialise and return the dictrionary

    
def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]


