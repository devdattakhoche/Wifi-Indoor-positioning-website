import traceback
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("ServiceKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



def get_all_active_paitent():
	"""
	:param: None
	returns : List of all patients
	"""
	try:
		collection = db.collection(u'active_patients')
		all_patients = list(map(lambda x: x.to_dict(), collection.stream()))
		return all_patients
	except Exception as ex:		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False
# get_all_active_paitent()


def get_active_paitent(uid):
	"""
	:param: uid
	returns : patient document
	"""
	try:
		doc_ref = db.collection(u'active_patients').document(uid)
		
		if doc_ref.get().to_dict() is None:
			raise Exception("No such patient found")
		return doc_ref.get().to_dict()
	except Exception as ex:		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

def get_blacklist():
	"""
	:param: None
	returns : List of all blacklist patients
	"""
	try:
		collection = db.collection(u'blacklist')
		all_patients = list(map(lambda x: x.to_dict(), collection.stream()))
		for i in all_patients:
			i['patient_details'] = get_active_paitent(i['patientId'])
		return all_patients
	except Exception as ex:		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False		


def Check_breach(uid):
	"""
	Returns boolean value if the patient breached or not in the database
	"""
	try:
		doc_ref = db.collection(u'blacklist')
		snapshots = list(doc_ref.where(u'patientId', u'==', uid).stream())
		if snapshots[0] is None:
			return False
		else:
			return snapshots[0].to_dict()
	except IndexError :
		return False
	except Exception as ex:
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False
	