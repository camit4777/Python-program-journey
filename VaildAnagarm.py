def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "listen"
    t = "silent"
    print("Is anagram:", is_anagram(s, t))  # Output: True