def decode_unicode(obj):
    if isinstance(obj, dict):
        return {k: decode_unicode(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [decode_unicode(item) for item in obj]
    elif isinstance(obj, str):
        return obj.encode('utf-8').decode('utf-8')
    else:
        return obj