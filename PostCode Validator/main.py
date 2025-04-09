import PostCodeValidator
import PostCodeLookUp

""" Rules for UK Post Codes
#1 - Postcodes are 5 to 7 characters long.
#2 - They always contain a mix of letters and numbers.
#3 - Valid Formats, Postcodes follow specific patterns, including:A9 9AA, A9A 9AA, A99 9AA, AA9 9AA, AA9A 9AA, AA99 9AA
#4 - Outward Code Rules - The first part (outward code) can be 2 to 4 characters., The first character is always a letter., The second character (if present) can be a letter or number., If there is a third character, it must be a number., The outward code always ends with a number.
#5 - Inward Code Rules: - The second part (inward code) is always three characters: a number followed by two letters (e.g., 9AA)., The first character is always a number (1-9)., The last two characters are always letters.
#6 - Spacing: - A single space must separate the outward and inward code (e.g., SW1A 1AA).
#7 - Special Cases: - Some areas have unique postcodes BF postcodes for British Forces
"""

if __name__ == '__main__':
    while True:
        postcode_input = input("Enter Post Code:") # user inputs post code

        validated_post_code = PostCodeValidator.validate_post_code_pattern(postcode_input) # validate post pattern is correct, from input

        if validated_post_code: # if the post pattern is valid and we search to see if postcode is correct
            PostCodeLookUp.get_postcode_information(validated_post_code)

        input_again = input("Enter Post Code again (Y):(N)") # input again option for user

        if input_again == "N" or input_again == "n": # click n/N to break cycle
            break