from database import db

def insert_document(collection_name, document_data):
    collection = db.get_collection(collection_name)
    result = collection.insert_one(document_data)
    print(result.inserted_id)

def read_document(collection_name, filter_query={}):
    collection = db.get_collection(collection_name)
    result = collection.find(filter_query)
    print(collection_name)
    for doc in result:
        print(doc)
    print("-----------------------------------")

def update_document(collection_name, filter_query, updated_data):
    collection = db.get_collection(collection_name)
    result = collection.update_one(filter_query, {"$set": updated_data})
    print(result.update_info)

def delete_document(collection_name, filter_query):
    collection = db.get_collection(collection_name)
    result = collection.delete_one(filter_query)
    print(result.deleted_count)