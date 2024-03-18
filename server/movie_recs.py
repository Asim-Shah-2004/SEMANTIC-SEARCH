#bug fix left do not touch



import pymongo
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URL"))
db = client.sample_mflix
collection = db.movies

embedding_url = os.getenv("HUGGING_FACE_URL")
token = os.getenv("TOKEN")


def generate_embedding(text: str) -> list[float]:
    payload = {"source_sentence": text, "sentences": [text]}
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {token}"},
        json=payload)

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# for doc in collection.find({'plot':{"$exists": True}}).limit(50):
#   doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
#   collection.replace_one({'_id': doc['_id']}, doc)

# query = "Among the residents of a theatrical boarding house is the last member of a once great acting family, down on his luck."

# results = collection.aggregate([
#   {"$vectorSearch": {
#     "queryVector": generate_embedding(query),
#     "path": "plot_embedding_hf",
#     "numCandidates": 100,
#     "limit": 4,
#     "index": "default",
#       }}
# ])

# for document in results:
#     print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')