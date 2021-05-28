#!/usr/bin/env python3

import psutil #install psutil
import schedule #install schedule
import time
import socket
import emails


def check_health():
    sender = 'automation@example.com'
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = 'Please check your system and resolve the issue as soon as possible.'

    if psutil.cpu_percent() > 80:
        message = emails.generate(sender, recipient, 'Error - CPU usage is over 80%', body, None)
        emails.send(message)
    else:
        pass
    if psutil.virtual_memory().available >> 20 < 500:
        emails.generate(sender, recipient, 'Error - Available memory is less than 500MB', body, None)
        emails.send(message)
    else:
        pass
    if psutil.disk_usage('/').percent > 80:
        emails.generate(sender, recipient, 'Error - Available disk space is less than 20%', body, None)
        emails.send(message)
    else:
        pass
    if socket.gethostbyname(socket.gethostname()) != '127.0.0.1':
        emails.generate(sender, recipient, 'Error - localhost cannot be resolved to 127.0.0.1', body, None)
        emails.send(message)

schedule.every(59).seconds.do(check_health)

while 1:
    schedule.run_pending()
    time.sleep(1)
