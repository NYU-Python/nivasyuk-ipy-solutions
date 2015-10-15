import argparse

#---------------------------------------------------------------------------#


def read_file(file_name):

    with open(file_name) as fh:
        lines = fh.readlines()

    return lines


def parse_header(header, data_field):

    fields = header.split('\t')
    field_index = fields.index(data_field)

    return field_index


def parse_data(data_lines, field_index):

    values = []

    for line in data_lines:
        split_data = line.split('\t')
        value = split_data[field_index]
        values.append(value)

    return values


def main(file_name, data_field):

    lines = read_file(file_name)
    field_index = parse_header(lines[0], data_field)
    values = parse_data(lines[1:], field_index)
    unique_values = set(values)

    print sorted(unique_values)


#---------------------------------------------------------------------------#

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='homework.2.2')
    parser.add_argument('file_name', type=str,
                        help="- name of bitly data file")
    parser.add_argument('data_field', type=str,
                        help="- data field to read")

    args = parser.parse_args()

    try:
        main(args.file_name, args.data_field)

    except Exception as e:
        print "Error: ", e
        parser.print_usage()

