#!/usr/bin/#!/usr/bin/env python3

import os
from datetime import datetime
import reports
import emails


def process_data(description_files):

    data = []
    for item in description_files:
        items = [i.strip() for i in f.readlines()]
        data.append(item[0] + '<br/>' + item[1] + '<br/><br/>')

    return data

def main():

    description_files = '/supplier-data/descriptions/'
    current_date = datetime.today().strftime('%Y-%m-%d')
    paragraph_data = process_data(description_files)
    title = 'Processed Update on ' + current_date
    email_text = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    reports.generate_report('/tmp/processed.pdf', title, str(paragraph_data))

    message = emails.generate('automation@example.com',  "{}@example.com".format(os.environ.get('USER')), 'Upload Completed - Online Fruit Store', email_text, '/tmp/processed.pdf')
    emails.send(message)

if __name__ == "__main__":
        main()
