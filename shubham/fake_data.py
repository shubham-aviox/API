from faker import Faker
from .db_orm import get_distributor_id, get_user_id, get_document_id, get_user_upload_user_id, get_customer_id, get_distributor_admin_distributor_id, get_user_id_distributor_admin, get_country_id

faker = Faker()

class FakeData(object):
    def __init__(self) -> None:
        self.name = faker.first_name(),
        self.contact_number = "+918790765689"
        self.phone_number = faker.postcode() + faker.postcode()
        self.email = faker.email()
        self.address = faker.address()
        self.pin_code = faker.postcode()
        self.country_id = "840ca6eb-324e-4cad-9100-c151e0f4f657"
        self.state_id = "94607cd2-520f-4db9-8e7c-3fdf989a9be4"
        self.city = faker.city()
        self.type = "nda"
        self.logo = faker.image_url()
        self.distributor_id = str(get_distributor_id())
        self.distributor_admin_distributor_id = str(get_distributor_admin_distributor_id(root_user=False))
        self.role_distributor_admin_distributor_id = str(get_distributor_admin_distributor_id(root_user=True))
        self.user_id = str(get_user_id())
        self.user_upload_user_id = str(get_user_upload_user_id())
        self.document_id = str(get_document_id(reject=False))
        self.rejected_document_id = str(get_document_id(reject=True))
        self.customer_id = str(get_customer_id())
        self.distributor_admin_user_id = str(get_user_id_distributor_admin())
        self.country_id = str(get_country_id())

fake_data_obj: FakeData = FakeData()