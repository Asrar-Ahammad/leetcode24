import string


def is_palindrome(s: str) -> bool:
    s = s.lower()
    a = ""
    for i in s:
        if i in string.punctuation or i == " ":
            continue
        else:
            a += i

    print(a, "->", a[::-1])
    return a == a[::-1]


print(is_palindrome(s="A man, a plan, a canal: Panama"))
print(is_palindrome(s="race a car"))
