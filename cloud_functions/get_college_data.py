
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json


cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
# Use a service account
'''
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'course_data').document('100')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')
'''

def get_data(request):
    '''
    try:
        req_id = str(request.form.get('req_id'))
        cred = credentials.Certificate('serviceAccount.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except:
        pass
        db = firestore.client()
    '''
        # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.

    # Set CORS headers for the preflight request
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
    req_id = str(request.args.get('req_id'))
    doc_ref = db.collection(u'course_data').document(req_id)

    doc = doc_ref.get()
    return(json.dumps(doc.to_dict()),200,headers)
