import uuid

def get_random_id():
    id = str(uuid.uuid4().hex[:8])