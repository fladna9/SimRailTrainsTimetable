import json
from routes.error_handlers import error_catcher


def get_train(train_number=None):
    train_number = "24181"
    try:
        with open('examples/' + train_number + '.json', 'r') as sample_file:
            stops = json.load(sample_file)
    except:
        return error_catcher()
    return stops
