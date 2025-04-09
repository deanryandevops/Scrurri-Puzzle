import re # regex

validPostCodePattern = "[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{1,2}" # regex pattern for Valid UK Post Code patterns
specialPostCodePattern = r"BFPO? [1-9][1-9]{1,3}[A-Z]{0,2}" #special British Airfoce postcode format
combinedPattern = f"({validPostCodePattern}|{specialPostCodePattern})"

def post_code_valid(pattern, postcode): # checking if the inputted post code matches the valid pattern, returns bool
    if re.fullmatch(pattern, postcode):
        print("Format is valid")
        return True
    else:
        print("Format is invalid")
        return False

def format_postcode_to_upper_text(postcode): # sets chars to upper
    return postcode.upper()

def strip_trailing_spaces_postcode(postcode): # removes spaces at start and end
    remove_trailing_spaces = postcode.strip()
    return remove_trailing_spaces

def remove_special_chars(postcode): # removes the special characters expect number, space and alphabet
    remove_special_chars_postcode = re.sub(r'[^A-Z0-9\s]', '', postcode)
    return remove_special_chars_postcode

def validate_post_code_pattern(postcode): # set the post code to correct format and validating postcode pattern
    postcode = format_postcode_to_upper_text(postcode)
    postcode = remove_special_chars(postcode)
    postcode = strip_trailing_spaces_postcode(postcode)
    post_code_valid(combinedPattern, postcode)
    return postcode