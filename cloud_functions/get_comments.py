import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_comments(request):
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    comments_arr = []
    req_id = str(request.args.get('req_id'))
    doc_ref = db.collection(u'comments').document(req_id).collections()
    for collection in doc_ref:
        for document in collection.stream():
            comment_dict = dict({"uid":document.id}, **document.to_dict())
            comments_arr.append(comment_dict)
    return (json.dumps(comments_arr), 200, headers)
            

