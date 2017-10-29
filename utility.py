import configurations


def replace_placeholders_in_string(string_with_placeholders, placeholder_replacements):
    """Replace placeholders of the type {X} with the X element in the array"""
    string_with_placeholders_replaced = string_with_placeholders
    for ctr in range(len(placeholder_replacements)):
        string_with_placeholders_replaced = string_with_placeholders_replaced.replace("{" + str(ctr) + "}", placeholder_replacements[ctr])

    return string_with_placeholders_replaced


def write_text_to_file(text_to_write):
    """Writes the text to the file whose details is present in configurations"""
    if text_to_write:
        f = open(configurations.output_file_location, "w")
        f.write(text_to_write)
        f.close()
        print "Writing to file complete..."
