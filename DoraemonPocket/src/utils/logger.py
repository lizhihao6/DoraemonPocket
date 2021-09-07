def log_error(msg, fn=None):
    if fn is None:
        return msg
    return msg+"\n"+fn.__doc__