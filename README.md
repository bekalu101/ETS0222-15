capitalize() – Capitalizes only the first letter of the string

text = "hello world"
print(text.capitalize())  # Output: "Hello world

second commit
Explanation of .replace(old, new)

The .replace(old, new) method is a powerful string manipulation function that finds and replaces all occurrences of a specific substring (old) within a string with another substring (new). It's a key tool for modifying string content, correcting errors, or standardizing text.

•  Purpose: To globally substitute one substring for another within a string, enabling easy modification and transformation of text data.

•  How it Works:

  1. The method scans the entire string, searching for instances of the old substring.
  2. For each occurrence of old that it finds, it replaces that substring with the new substring.
  3. The process continues until all instances of old have been replaced.
  4. A new string is returned with the replacements made. The original string is typically not modified (strings are often immutable).

•  old Substring: The substring you want to find and replace.

•  new Substring: The substring that will replace each occurrence of the old substring.

•  Case Sensitivity: The replacement is usually case-sensitive (e.g., "hello" will not match "Hello"). Some languages may provide case-insensitive versions of the replace method (or you can use .lower() or .upper() to normalize case before replacing).

•  No Occurrences: If the old substring is not found in the string, the method returns the original string unchanged.

Example (Python):

# Basic replacement:
text = "Hello world"
new_text = text.replace("Hello", "Hi")  # new_text will be "Hi world"

# Replacing multiple occurrences:
text = "apple banana apple cherry apple"
new_text = text.replace("apple", "orange")  # new_text will be "orange banana orange cherry orange"

# Replacing with an empty string (effectively deleting):
text = "Remove this word"
new_text = text.replace("Remove ", "")  # new_text will be "this word"

# No occurrences found:
text = "Hello world"
new_text = text.replace("Goodbye", "Hi")  # new_text will be "Hello world" (no change)

# Case sensitivity:
text = "The quick brown fox jumps over the Lazy Dog"
new_text = text.replace("the", "a")  # new_text will be "The quick brown fox jumps over a Lazy Dog" (only the lowercase "the" is 


third commit
# Uppercase String Utility

"""
## Overview
This module provides a function to convert a string to uppercase using Python's built-in `upper()` method.

## Features
- Converts all lowercase letters to uppercase.
- Leaves non-alphabetic characters unchanged.
- Useful for text standardization and formatting.

## Function Definition
```python
def to_uppercase(text: str) -> str:
    """Converts the given string to uppercase."""
    return text.upper()
```

## Example Usage
```python
if __name__ == "__main__":
    sample_text = "hello world"
    print(to_uppercase(sample_text))  # Output: "HELLO WORLD"

    sample_text = "Python is Awesome!"
    print(to_uppercase(sample_text))  # Output: "PYTHON IS AWESOME!"
```

## Use Cases
- Formatting user input.
- Making case-insensitive comparisons.
- Displaying text in uppercase for readability.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- It works with any string input, including mixed-case or special characters.


fourth commit
# Lowercase String Utility

"""
## Overview
This module provides a function to convert a string to lowercase using Python's built-in `lower()` method.

## Features
- Converts all uppercase letters to lowercase.
- Leaves non-alphabetic characters unchanged.
- Useful for text standardization and case-insensitive comparisons.

## Function Definition
```python
def to_lowercase(text: str) -> str:
    """Converts the given string to lowercase."""
    return text.lower()
```

## Example Usage
```python
if __name__ == "__main__":
    sample_text = "HELLO WORLD"
    print(to_lowercase(sample_text))  # Output: "hello world"
```

## Use Cases
- Formatting user input for consistency.
- Making case-insensitive string comparisons.
- Standardizing text data for storage and retrieval.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- It works with any string input, including mixed-case, numbers, or special characters.
"""


fifth commit
# Title Case String Utility

"""
## Overview
This module provides a function to convert a string to title case using Python's built-in `title()` method.

## Features
- Capitalizes the first letter of each word.
- Converts the rest of the letters in each word to lowercase.
- Useful for formatting titles, names, and headings.

## Function Definition
```python
def to_title_case(text: str) -> str:
    """Converts the given string to title case."""
    return text.title()
```

## Example Usage
```python
if __name__ == "__main__":
    sample_text = "hello world from python"
    print(to_title_case(sample_text))  # Output: "Hello World From Python"
```

## Use Cases
- Formatting names, titles, and headings.
- Standardizing text for readability.
- Enhancing text presentation in documents and applications.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Works best with standard sentence formatting but may not handle special cases like "McDonald's" correctly.
"""


six commite
# Swapcase String Utility

"""
## Overview
This module provides a function to swap the case of letters in a string using Python's built-in `swapcase()` method.

## Features
- Converts **uppercase letters** to **lowercase**.
- Converts **lowercase letters** to **uppercase**.
- Leaves non-alphabetic characters unchanged.
- Useful for toggling text case and formatting.

## Function Definition
```python
def swap_case(text: str) -> str:
    """Swaps uppercase and lowercase letters in a string."""
    return text.swapcase()
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Basic case swapping
    sample_text = "Hello World"
    print(swap_case(sample_text))  # Output: "hELLO wORLD"

    # Example 2: Mixed case
    sample_text = "PyThOn PrOgRaMmInG"
    print(swap_case(sample_text))  # Output: "pYtHoN pRoGrAmMiNg"

    # Example 3: String with numbers and symbols
    sample_text = "123 Hello!"
    print(swap_case(sample_text))  # Output: "123 hELLO!"
```

## Use Cases
- Formatting text to alternate between cases.
- Improving readability in special applications.
- Processing text for encryption or coding puzzles.
- Creating stylistic text for display purposes.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Works with any string input, including mixed-case, numbers, or special characters.

"""


seven commit
# Strip String Utility

"""
## Overview
This module provides a function to remove leading and trailing spaces from a string using Python's built-in `strip()` method.

## Features
- Removes **leading spaces** (spaces at the beginning of the string).
- Removes **trailing spaces** (spaces at the end of the string).
- Leaves spaces between words **unchanged**.
- Useful for cleaning up user input or formatting text data.

## Function Definition
```python
def strip_text(text: str) -> str:
    """Removes leading and trailing spaces from a string."""
    return text.strip()
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Basic trimming
    sample_text = "   Hello World   "
    print(strip_text(sample_text))  # Output: "Hello World"

    # Example 2: String with only spaces
    sample_text = "      "
    print(strip_text(sample_text))  # Output: "" (Empty string)

    # Example 3: String with spaces in between words
    sample_text = "  Python Programming  "
    print(strip_text(sample_text))  # Output: "Python Programming"
```

## Use Cases
- Cleaning user input to remove unintended spaces.
- Formatting text data for consistency.
- Preprocessing text before storing in a database.
- Standardizing output for better readability.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Works with any string input, including spaces, numbers, or special characters.



eight commit
# Lstrip String Utility

"""
## Overview
This module provides a function to remove leading spaces (spaces from the left side) from a string using Python's built-in `lstrip()` method.

## Features
- Removes **leading spaces** (spaces at the beginning of the string).
- Leaves **trailing spaces** and spaces between words **unchanged**.
- Useful for cleaning up user input or formatting text data.

## Function Definition
```python
def lstrip_text(text: str) -> str:
    """Removes leading spaces from a string."""
    return text.lstrip()
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Basic trimming from the left
    sample_text = "   Hello World   "
    print(lstrip_text(sample_text))  # Output: "Hello World   "

    # Example 2: String with only spaces
    sample_text = "      "
    print(lstrip_text(sample_text))  # Output: "" (Empty string)

    # Example 3: String with spaces in between words
    sample_text = "  Python Programming  "
    print(lstrip_text(sample_text))  # Output: "Python Programming  "
```

## Use Cases
- Cleaning user input to remove unintended leading spaces.
- Formatting text data for consistency.
- Preprocessing text before storing in a database.
- Standardizing output for better readability.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Works with any string input, including spaces, numbers, or special characters.
"""


ninth commit
# Rstrip String Utility

"""
## Overview
This module provides a function to remove trailing spaces (spaces from the right side) from a string using Python's built-in `rstrip()` method.

## Features
- Removes **trailing spaces** (spaces at the end of the string).
- Leaves **leading spaces** and spaces between words **unchanged**.
- Useful for cleaning up user input or formatting text data.

## Function Definition
```python
def rstrip_text(text: str) -> str:
    """Removes trailing spaces from a string."""
    return text.rstrip()
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Basic trimming from the right
    sample_text = "   Hello World   "
    print(rstrip_text(sample_text))  # Output: "   Hello World"

    # Example 2: String with only spaces
    sample_text = "      "
    print(rstrip_text(sample_text))  # Output: "" (Empty string)

    # Example 3: String with spaces in between words
    sample_text = "  Python Programming  "
    print(rstrip_text(sample_text))  # Output: "  Python Programming"
```

## Use Cases
- Cleaning user input to remove unintended trailing spaces.
- Formatting text data for consistency.
- Preprocessing text before storing in a database.
- Standardizing output for better readability.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Works with any string input, including spaces, numbers, or special characters.
"""


tenth commit
# Zfill String Utility

"""
## Overview
This module provides a function to pad a string with leading zeros to reach a specified width using Python's built-in `zfill()` method.

## Features
- Pads the string with leading zeros until it reaches the specified width.
- Retains existing characters without modification.
- Useful for formatting numbers, aligning text, and ensuring uniform string length.

## Function Definition
```python
def zfill_text(text: str, width: int) -> str:
    """Pads the string with leading zeros to reach the given width."""
    return text.zfill(width)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Padding a number string
    sample_text = "42"
    print(zfill_text(sample_text, 5))  # Output: "00042"

    # Example 2: Padding a longer string (no change if already equal or greater than width)
    sample_text = "hello"
    print(zfill_text(sample_text, 3))  # Output: "hello"

    # Example 3: Padding a negative number
    sample_text = "-42"
    print(zfill_text(sample_text, 5))  # Output: "-0042"
```

## Use Cases
- Formatting numerical values for display (e.g., invoice numbers, serial codes).
- Ensuring fixed-length strings for data processing.
- Standardizing input fields where a specific width is required.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Works with both numeric and non-numeric strings.
- If the string already meets or exceeds the specified width, no padding is applied.
"""

eleventh commit
# Center String Utility

"""
## Overview
This module provides a function to center a string within a specified width using a given padding character, utilizing Python's built-in `center()` method.

## Features
- Centers the string within the specified width.
- Pads with a specified character to fill the extra space.
- Useful for formatting output and aligning text in tables or UI displays.

## Function Definition
```python
def center_text(text: str, width: int, char: str = ' ') -> str:
    """Centers the string within the given width using the specified padding character."""
    return text.center(width, char)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Centering with default space padding
    sample_text = "Hello"
    print(center_text(sample_text, 10))  # Output: "  Hello   "

    # Example 2: Centering with custom padding character
    sample_text = "Python"
    print(center_text(sample_text, 12, '*'))  # Output: "***Python***"

    # Example 3: Width smaller than string length (no change)
    sample_text = "LongText"
    print(center_text(sample_text, 5, '-'))  # Output: "LongText"
```

## Use Cases
- Formatting headers in text-based applications.
- Aligning text in table-like structures.
- Enhancing the visual appearance of printed or displayed text.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- If the specified width is smaller than the string length, no padding is applied.
- The padding character must be a single character string.
"""

tweleveth commit
# Rjust String Utility

"""
## Overview
This module provides a function to right-align a string within a specified width using a given padding character, utilizing Python's built-in `rjust()` method.

## Features
- Right-aligns the string within the specified width.
- Pads with a specified character to fill the extra space.
- Useful for formatting output and aligning text in tables or UI displays.

## Function Definition
```python
def rjust_text(text: str, width: int, char: str = ' ') -> str:
    """Right-aligns the string within the given width using the specified padding character."""
    return text.rjust(width, char)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Right-aligning with default space padding
    sample_text = "Hello"
    print(rjust_text(sample_text, 10))  # Output: "     Hello"

    # Example 2: Right-aligning with custom padding character
    sample_text = "Python"
    print(rjust_text(sample_text, 12, '*'))  # Output: "******Python"

    # Example 3: Width smaller than string length (no change)
    sample_text = "LongText"
    print(rjust_text(sample_text, 5, '-'))  # Output: "LongText"
```

## Use Cases
- Formatting numerical values for alignment.
- Aligning text in reports, tables, or console output.
- Ensuring consistent text layout in text-based applications.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- If the specified width is smaller than the string length, no padding is applied.
- The padding character must be a single character string.
"""

thirteen commit
# Ljust String Utility

"""
## Overview
This module provides a function to left-align a string within a specified width using a given padding character, utilizing Python's built-in `ljust()` method.

## Features
- Left-aligns the string within the specified width.
- Pads with a specified character to fill the extra space.
- Useful for formatting output and aligning text in tables or UI displays.

## Function Definition
```python
def ljust_text(text: str, width: int, char: str = ' ') -> str:
    """Left-aligns the string within the given width using the specified padding character."""
    return text.ljust(width, char)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Left-aligning with default space padding
    sample_text = "Hello"
    print(ljust_text(sample_text, 10))  # Output: "Hello     "

    # Example 2: Left-aligning with custom padding character
    sample_text = "Python"
    print(ljust_text(sample_text, 12, '*'))  # Output: "Python******"

    # Example 3: Width smaller than string length (no change)
    sample_text = "LongText"
    print(ljust_text(sample_text, 5, '-'))  # Output: "LongText"
```

## Use Cases
- Formatting text output for alignment.
- Aligning text in tables, reports, or console output.
- Ensuring consistent text layout in text-based applications.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- If the specified width is smaller than the string length, no padding is applied.
- The padding character must be a single character string.
"""

fourteen commit
# Find String Utility

"""
## Overview
This module provides a function to locate the first occurrence of a substring within a string using Python's built-in `find()` method.

## Features
- Returns the index of the first occurrence of a substring.
- Returns `-1` if the substring is not found.
- Useful for searching and extracting data from text.

## Function Definition
```python
def find_substring(text: str, substring: str) -> int:
    """Finds the first occurrence of a substring and returns its index, or -1 if not found."""
    return text.find(substring)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Substring found
    sample_text = "Hello, welcome to Python programming."
    print(find_substring(sample_text, "Python"))  # Output: 18

    # Example 2: Substring not found
    print(find_substring(sample_text, "Java"))  # Output: -1

    # Example 3: Searching for a single character
    print(find_substring(sample_text, "w"))  # Output: 7

    # Example 4: Searching for a word at the beginning
    print(find_substring(sample_text, "Hello"))  # Output: 0
```

## Use Cases
- Checking if a specific word exists in a string.
- Extracting parts of a text based on keyword position.
- Implementing basic search functionality in text-processing applications.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Indexing starts at `0`, meaning the first character of the string has index `0`.
- If multiple occurrences exist, only the index of the first one is returned.
"""

fifteen commit
# Index String Utility

"""
## Overview
This module provides a function to locate the first occurrence of a substring within a string using Python's built-in `index()` method.

## Features
- Returns the index of the first occurrence of a substring.
- Raises a `ValueError` if the substring is not found.
- Useful for searching and extracting data from text.

## Function Definition
```python
def index_substring(text: str, substring: str) -> int:
    """Finds the first occurrence of a substring and returns its index, or raises an error if not found."""
    return text.index(substring)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Substring found
    sample_text = "Hello, welcome to Python programming."
    print(index_substring(sample_text, "Python"))  # Output: 18

    # Example 2: Substring not found (raises ValueError)
    try:
        print(index_substring(sample_text, "Java"))  # Raises ValueError
    except ValueError:
        print("Substring not found!")

    # Example 3: Searching for a single character
    print(index_substring(sample_text, "w"))  # Output: 7

    # Example 4: Searching for a word at the beginning
    print(index_substring(sample_text, "Hello"))  # Output: 0
```

## Use Cases
- Ensuring a substring exists before processing it.
- Extracting parts of text based on keyword position.
- Implementing precise search functionality in text-processing applications.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Indexing starts at `0`, meaning the first character of the string has index `0`.
- If the substring is not found, a `ValueError` is raised.
"""

sixteen commit
# Rfind String Utility

"""
## Overview
This module provides a function to locate the last occurrence of a substring within a string using Python's built-in `rfind()` method.

## Features
- Returns the index of the last occurrence of a substring.
- Returns `-1` if the substring is not found.
- Useful for reverse searching within text data.

## Function Definition
```python
def rfind_substring(text: str, substring: str) -> int:
    """Finds the last occurrence of a substring and returns its index, or -1 if not found."""
    return text.rfind(substring)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Substring found multiple times
    sample_text = "Python is fun, and learning Python is great!"
    print(rfind_substring(sample_text, "Python"))  # Output: 27

    # Example 2: Substring not found
    print(rfind_substring(sample_text, "Java"))  # Output: -1

    # Example 3: Searching for a single character
    print(rfind_substring(sample_text, "n"))  # Output: 36

    # Example 4: Searching for a word at the beginning
    print(rfind_substring(sample_text, "fun"))  # Output: 10
```

## Use Cases
- Finding the last occurrence of a keyword in a document.
- Extracting text from the last instance of a specific delimiter.
- Reverse searching for patterns in log files or reports.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Indexing starts at 0, meaning the first character of the string has index 0.
- If multiple occurrences exist, only the index of the last one is returned.
"""

seventeen commit
# Replace String Utility

"""
## Overview
This module provides a function to replace all occurrences of a substring within a string using Python's built-in `replace()` method.

## Features
- Replaces all occurrences of a specified substring with another.
- Returns a new string with replacements applied.
- Useful for text modifications and data cleaning.

## Function Definition
```python
def replace_substring(text: str, old: str, new: str) -> str:
    """Replaces all occurrences of a substring with another."""
    return text.replace(old, new)
```

## Example Usage
```python
if __name__ == "__main__":
    # Example 1: Basic replacement
    sample_text = "Hello, world!"
    print(replace_substring(sample_text, "world", "Python"))  # Output: "Hello, Python!"

    # Example 2: Replacing multiple occurrences
    sample_text = "apple banana apple cherry apple"
    print(replace_substring(sample_text, "apple", "orange"))  # Output: "orange banana orange cherry orange"

    # Example 3: Removing a word by replacing with an empty string
    sample_text = "Remove this word"
    print(replace_substring(sample_text, "Remove ", ""))  # Output: "this word"
```

## Use Cases
- Correcting spelling or formatting mistakes.
- Standardizing text data for consistency.
- Removing unwanted words or characters from strings.

## Notes
- The function does not modify the original string (strings in Python are immutable).
- Replacements are case-sensitive.
- If the `old` substring is not found, the original string remains unchanged.