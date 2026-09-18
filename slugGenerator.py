'''
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.

'''


def generate_slug(string):

    string = string.lower()
    clean = ''.join(c for c in string if c.isalnum() or c == ' ')
    clean_new = clean.split()
    return "%20".join(clean_new)


print(generate_slug("helloWorld")) #should return "helloworld".
print(generate_slug("hello world!")) #should return "hello%20world".
print(generate_slug(" hello-world ")) #should return "helloworld".
print(generate_slug("hello  world")) #should return "hello%20world".
print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ")) #should return "h3110%20w0r1d"