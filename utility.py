import os
import webbrowser
import constants
import re


def replace_placeholders_in_string(string_with_placeholders, placeholder_replacements):
    """Replace placeholders of the type {X} with the X element in the array"""
    number_of_placeholder_replacements = len(placeholder_replacements)
    placeholder_pattern_groups = re.findall(constants.placeholders_regex, string_with_placeholders)
    placeholder_pattern_groups_count = len(placeholder_pattern_groups)
    if placeholder_pattern_groups_count != number_of_placeholder_replacements:
        raise ValueError()
    if placeholder_pattern_groups[0] != "{0}":
        raise IndexError()
    string_with_placeholders_replaced = string_with_placeholders
    for ctr in range(len(placeholder_replacements)):
        string_with_placeholders_replaced = string_with_placeholders_replaced.replace("{" + str(ctr) + "}",
                                                                                      placeholder_replacements[ctr])
    return string_with_placeholders_replaced


def write_text_to_file(text_to_write, complete_file_location):
    """Writes the text to the file whose details is present in configurations"""
    if text_to_write:
        f = open(complete_file_location, "w")
        f.write(text_to_write)
        f.close()
        print "Writing to file with name: " + complete_file_location + "complete..."


def open_file_path_in_browser(file_path):
    """Open the file path in a browser"""
    file_prefix = "file://"
    if file_path is not None:
        webbrowser.open(file_prefix + os.path.realpath(file_path))


def create_html_element_based_on_details(node_value, node_type, parent_node):
    """Create HTML element based on the details of the node value and the node type"""
    if node_type == constants.span_element or node_type == constants.p_element:
        parent_node.p(node_value)
    elif node_type == constants.img_element:
        parent_node.img("", src=node_value)
    elif node_type == constants.hyperlink_element:
        parent_node.a(node_value, href=node_value)
    else:
        parent_node.span(node_value)
