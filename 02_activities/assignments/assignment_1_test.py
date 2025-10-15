# Part 1: Base Anagram Checker
def anagram_checker(word_a, word_b):
    word_a_lower = word_a.lower()
    word_b_lower = word_b.lower()
    return sorted(word_a_lower) == sorted(word_b_lower)

# Test cases for Part 1
print(anagram_checker("Silent", "listen"))  # True
print(anagram_checker("Silent", "Night"))   # False
print(anagram_checker("night", "Thing"))    # True

# Part 2: Anagram Checker with Case Sensitivity
def anagram_checker(word_a, word_b, is_case_sensitive=False):
    if not is_case_sensitive:
        word_a = word_a.lower()
        word_b = word_b.lower()
    return sorted(word_a) == sorted(word_b)

# Test cases for Part 2
print(anagram_checker("Silent", "listen", False))  # True
print(anagram_checker("Silent", "Listen", True))   # False
print(anagram_checker("night", "Thing", False))    # True
