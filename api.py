from utils import mask_pii
from models import predict_category

def process_email(email_body: str):
    masked_email, entities = mask_pii(email_body)
    category = predict_category(masked_email)
    return {
        "input_email_body": email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
