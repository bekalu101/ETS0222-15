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