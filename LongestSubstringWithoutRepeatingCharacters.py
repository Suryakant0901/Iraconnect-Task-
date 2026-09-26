def solution(input):
    s = input["s"]

    seen = set()
    start = 0
    longest = 0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[start])
            start += 1

        seen.add(s[i])

        length = i - start + 1

        if length > longest:
            longest = length

    return longest
