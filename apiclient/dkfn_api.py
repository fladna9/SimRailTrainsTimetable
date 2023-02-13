import requests
from app import error_catcher


DKFN_API = "https://sr-dispatch-api-staging-uld3cp3nxa-od.a.run.app/train/"


def get_train(train_number=None):
    try:
        timetable_response = requests.get(DKFN_API + train_number)
        if timetable_response.status_code != 200 or timetable_response is None:
            raise Exception("No response from dkfnAPI")
    except:
        error_catcher()
    return timetable_response.json()
