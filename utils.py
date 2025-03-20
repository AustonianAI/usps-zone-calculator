def find_zone_row(origin_zip):
    """
    Find the row in the zone matrix for the given origin zip code.
    """
    zip_prefix = origin_zip.strip()[:3]
    print(f"zip_prefix: {zip_prefix}")

    with open('Format2.txt', 'r') as file:
        for line_number, line in enumerate(file, 1):
            # Check characters at positions 1-3 (index 0-2)
            if line[0:3] == zip_prefix:
                print(f"Found matching row at line {line_number}")
                return line

    # If no match is found
    raise ValueError(f"No zone found for ZIP prefix {zip_prefix}")


def determine_zone_column(destination_zip):
    """
    Determine the column in the zone matrix for the given destination zip code.
    """
    zip_prefix = destination_zip.strip()[:3]
    print(f"zip_prefix: {zip_prefix}")

    # Check if the prefix can be converted to an integer
    try:
        prefix_num = int(zip_prefix)
        column = ((prefix_num - 1) * 2) + 4
        print(f"Column position: {column}")
        return column
    except ValueError:
        raise ValueError(f"ZIP prefix {zip_prefix} is not a valid number")


def get_zone_from_row_and_column(row, column):
    """
    Get the zone from the row and column in the zone matrix.

    We need to subtract 1 from the column because the column index is 0-based.
    """
    return row[column-1]
