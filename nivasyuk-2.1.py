#!/usr/bin/env python

import os
import sys

sendmail_prog = '/usr/sbin/sendmail'

#---------------------------------------------------------------------------#


def parse_args(args):

    result = {}

    for arg in args:
        parts = arg.split('=')

        if len(parts) != 2:
            raise Exception("Invalid format: {0}".format(arg))

        if parts[0] in result:
            raise Exception("'{0}' already specified".format(parts[0]))

        result[parts[0]] = parts[1]

    return result


def validate_args(parsed_args):

    required_args = {'to', 'from'}
    valid_args = {'to', 'from', 'subject', 'body'}
    parsed_keys = set(parsed_args.keys())

    if not (parsed_keys <= valid_args):
        invalid_args = parsed_keys - valid_args
        raise Exception('Invalid args: {0}'.format(invalid_args))

    if not (required_args <= parsed_keys):
        missing_args = required_args - parsed_keys
        raise Exception('Required args missing: {0}'.format(missing_args))


def get_header(parsed_args):

    header = ""

    header += "From: {0}\n".format(parsed_args['from'])
    header += "To: {0}\n".format(parsed_args['to'])

    if 'subject' in parsed_args:
        header += "Subject: {0}\n".format(parsed_args['subject'])

    return header


def send_email(header, body):

    msg = header + body
    #print msg

    sendmail = os.popen(sendmail_prog + " -t", "w")
    sendmail.write(msg)
    sendmail.close()


def main(args):

    parsed_args = parse_args(args)
    validate_args(parsed_args)
    header = get_header(parsed_args)

    print header

    send_email(header, parsed_args.get('body', ''))


#---------------------------------------------------------------------------#


if __name__ == "__main__":

    args = sys.argv[1:]

    try:
        main(args)

    except Exception as e:
        print "Error:", e



