from time import ctime

# change package_name to your package name.
from DoraemonPocket.version import VERSION


def run():
    cur_time = ctime()
    # change package_name to your package name.
    text = f"""
    # DoraemonPocket
    
    Version {VERSION} ({cur_time} +0800)
    """
    print(text)
