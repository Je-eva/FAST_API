from fastapi import APIRouter , HTTPException,status
from models.todo import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router=APIRouter()

@router.get("/")
async def get_todos():
#    Uses list_serial to serialize the results.

    todos= list_serial(collection_name.find())
    return todos
    #collection name is todo
    #find is used for getting eeceyrthing in the collecltion and return it
    
    
@router.put("/{id}")
async def update_todo(id: str, updated_todo: Todo):
    # Find the document with the matching _id
    existing_todo = collection_name.find_one({"_id": ObjectId(id)})

    if existing_todo:  # If the TODO exists
        # Update the document with new data
        collection_name.update_one(
            {"_id": ObjectId(id)},  # Find by _id
            {"$set": dict(updated_todo)}  # Update with new values
        )
        return {"message": "TODO updated successfully"}, status.HTTP_200_OK  # Return 200 status
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TODO not found"
        )


@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

@router.delete("/{id}")
async def delete(id: str):
        collection_name.find_one_and_delete({"_id": ObjectId(id )})
        