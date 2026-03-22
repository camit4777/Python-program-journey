def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:  # closing bracket
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:  # opening bracket
            stack.append(char)

    return not stack


if __name__ == "__main__":
    s = input("Enter brackets string: ")
    print("Valid" if is_valid(s) else "Invalid")