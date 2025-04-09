# Scrurri-Puzzles

### Automated Build Pipeline

I am very proud of building an automated pipeline using Unity, Jenkins, and C# for our many platforms. This solution eliminates repetitive tasks and human error by creating a parameterized build pipeline. Previously, builds were performed manually within the company, consuming a machine during the process. With this automation, efficiency has greatly improved.

### UK Post Code Validator

This application validates a UK postcode by ensuring it follows the correct pattern. It then calls an API to verify whether the validated postcode exists within the Royal Mail database.

Additionally, a library is available that supports validating and formatting UK postcodes. Details on valid postcodes and their components can be found at Wikipedia. The API design for this library is flexible and can be structured as needed.

#### Rules for UK Post Codes

- Postcodes are 5 to 7 characters long.

- They always contain a mix of letters and numbers.

- Valid Formats: Postcodes follow specific patterns, including: A9 9AA, A9A 9AA, A99 9AA, AA9 9AA, AA9A 9AA, AA99 9AA.

##### Outward Code Rules:

- The first part (outward code) can be 2 to 4 characters.

- The first character is always a letter.

- The second character (if present) can be a letter or number.

- If there is a third character, it must be a number.

- The outward code always ends with a number.

#### Inward Code Rules:

- The second part (inward code) is always three characters: a number followed by two letters (e.g., 9AA).

- The first character is always a number (1-9).

- The last two characters are always letters.

- Spacing: A single space must separate the outward and inward code (e.g., SW1A 1AA).

- Special Cases: Some areas have unique postcodes, such as BF postcodes for British Forces.

### Pre-requisite
- pip install requests
- To run the UK Post Code Validator, install the required dependency:

#### To Execute
##### Run the application
`python PostCodeValidator/main.py`

### ThreeFive Problem

Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Three" instead of the number, and for multiples of five, print "Five". For numbers that are multiples of both three and five, print "ThreeFive".

#### To Execute
##### Run the application
`python ThreeFiveProblem/main.py`
