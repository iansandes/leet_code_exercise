def reverseWords(s: str) -> str:
    s = s.split()
    s = s[::-1]
    s = (" ".join(s))
    return s


reverseWords("the sky is blue")

