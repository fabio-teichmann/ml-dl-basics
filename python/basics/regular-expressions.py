import re

pattern = re.compile(r"([a-zA-Z]).([a])")

text = 'search this inside of this string please!'

a = pattern.search(text)
print(a.span())
# print(a.start())
# print(a.end())
print(a.group())

b = pattern.findall(text)
print(b)
# needs to match the full text
c = pattern.fullmatch(text)

# can match partial (from start)
d = pattern.match(text)
print(d)
