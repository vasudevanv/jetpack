def pop_keys(d, keys, default=None):
    return [d.pop(k, default) for k in keys]

def get_items(collection, key, value):
    return next((item for item in collection if item[key] == value), None)