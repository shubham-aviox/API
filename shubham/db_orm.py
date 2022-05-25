from admin_distributor_application.models.distributor_portal.distributor_model import Distributor, User, UserUploads,SignzyVerificationLog, AgentNotes, DistributorAdmin, State
from admin_distributor_application.db_session import session

def get_distributor_id():
	""" Get distributor id """
	try:
		distributor = session.query(Distributor).filter(Distributor.is_deleted == False).first()
		return distributor.id
	except Exception as e:
		return str(e)


def get_user_id():
	""" Get user id """
	try:
		user = session.query(User).filter(User.is_deleted == False).first()
		return user.id
	except Exception as e:
		return str(e)


def get_user_upload_user_id():
	""" Get user id user upload """
	try:
		user_upload = session.query(UserUploads).filter(UserUploads.approval_status == "Approved").first()
		return user_upload.user_id
	except Exception as e:
		return str(e)


def get_document_id(reject=False):
	""" Get document id """
	try:
		if reject:
			document = session.query(UserUploads).filter(UserUploads.approval_status == "Rejected").first()
			return document.id
		else:
			document = session.query(UserUploads).filter(UserUploads.approval_status == "Approved").first()
			return document.id

	except Exception as e:
		return str(e)


def get_component_id():
	""" Get user id """
	try:
		user_upload = session.query(UserUploads).filter(UserUploads.approval_status == "Approved").first()
		return user_upload.id
	except Exception as e:
		return str(e)


def get_customer_id():
	""" Get customer id """
	try:
		customer = session.query(AgentNotes).first()
		return customer.customer_id
	except Exception as e:
		return str(e)


def get_distributor_admin_distributor_id(root_user=False):
	""" Get distributor admin distributor id """
	try:
		if root_user:
			distributor = session.query(DistributorAdmin).filter(DistributorAdmin.role == "root_user").filter(DistributorAdmin.is_deleted == False).filter(DistributorAdmin.distributor_id != None).first()
			return distributor.distributor_id
		else:
			distributor = session.query(DistributorAdmin).filter(DistributorAdmin.role != "root_user").filter(DistributorAdmin.is_deleted == False).filter(DistributorAdmin.distributor_id != None).first()
			return distributor.distributor_id
	except Exception as e:
		return str(e)


def get_user_id_distributor_admin():
	""" Get user id distributor admin """
	try:
		distributor_admin = session.query(DistributorAdmin).filter(DistributorAdmin.is_deleted == False).first()
		return distributor_admin.user_id
	except Exception as e:
		return str(e)


def get_country_id():
	""" Get user id distributor admin """
	try:
		state = session.query(State).filter(State.is_deleted == False).first()
		return state.country_id
	except Exception as e:
		return str(e)