import json
from bson import json_util


def session(func):
    def wrapper(*args, **kwargs):
        with args[0].client.start_session() as session:
            with session.start_transaction():
                try:
                    result = func(*args, **kwargs, session=session)
                    session.commit_transaction()
                    return result
                except Exception as e:
                    session.abort_transaction()
                    raise e

    return wrapper


def jsonResponse(result) -> dict:
    return json.loads(json_util.dumps(result))
