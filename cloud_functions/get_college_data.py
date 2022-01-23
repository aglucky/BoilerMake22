
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
    req_id = str(request.args.get('req_id'))
    doc_ref = db.collection(u'course_data').document(req_id)

    doc = doc_ref.get()
    return json.dumps(doc.to_dict())
