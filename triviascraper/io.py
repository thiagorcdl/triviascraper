"""
Helper functions for input and output.
"""
import csv

TMP_FILE = "/tmp/trivia.csv"
DELIMITER = " "
QUOTECHAR = "\""


def parse_params():
    """Change behavior based on passed options.

    TODO
    """
    return


def write_to_file(row_content,
                  filename=TMP_FILE):  # TODO: hook in filename from arguments
    """Save iterable to CSV.

    TODO: allow exporting to other formats.
    """
    with open(filename, mode="a") as output_file:
        writer = csv.writer(
            output_file,
            delimiter=DELIMITER,
            quoting=csv.QUOTE_ALL
        )
        writer.writerow(row_content)
