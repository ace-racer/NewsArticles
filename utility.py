def replace_placeholders_in_string(string_with_placeholders, placeholder_replacements):
    string_with_placeholders_replaced = string_with_placeholders
    for ctr in range(len(placeholder_replacements)):
        string_with_placeholders_replaced = string_with_placeholders_replaced.replace("{" + str(ctr) + "}", placeholder_replacements[ctr])

    return string_with_placeholders_replaced
