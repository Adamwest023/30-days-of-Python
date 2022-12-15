from datetime import datetime

from formatting import format_msg


def send(name, website):
    msg = format_msg(my_name=name, my_website=website)
    # send the message

    return msg
