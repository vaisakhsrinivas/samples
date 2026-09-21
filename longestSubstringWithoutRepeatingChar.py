def nonrepeat(s):

    left = 0
    longest = 0
    longeststring = ""
    sub = set()

    for right in range(len(s)):
        while s[right] in sub:
            sub.remove(s[left])
            left += 1
        sub.add(s[right])
        current = right - left + 1
        if current > longest:
            longest = current
            longeststring = s[left:right+1]
    return longeststring, longest


print(nonrepeat("abcabcbb"))
print(nonrepeat("bbbb"))
print(nonrepeat("abbadcbaaaabdcc"))

