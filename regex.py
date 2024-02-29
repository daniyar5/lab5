import re

#ex1
# text = "abbbabababbbabbaabb a"
# print("Match: ", re.match("ab*", text))


#ex2
# text = "abbbbbb"
# print("Match: ", re.match("ab{2,3}$", text))


#ex3
# text = input()
# pattern = r"[a-z]_+"
# print("Found: ", re.findall(pattern, text))

#ex4
# text = input()
# pattern = r"([A-Z][a-z]+)+"
# print("Found: ", re.findall(pattern, text))

#ex5
# text = input()
# pattern = r".+a.+b"
# print("Found: ", re.findall(pattern, text))

#ex6
# text = input()
# pattern = re.sub("[ ,.]", ":", text)
# print(pattern)

#ex7
# text = input()
# a = re.split("_", text)
# pattern = a[0] + a[1].capitalize()
# print(pattern)

#ex8
# text = input()
# pattern = re.findall('[A-Z][^A-Z]*', text)
# print(pattern)

#ex9
# text = input()
# pattern = re.findall('[A-Z][^A-Z]*', text)
# a = ' '.join((pattern))
# print(a)

#ex10
text = input()
pattern = re.findall('[a-zA-Z][a-z]*', text)
a = ' '.join((pattern))
b = re.sub(" ", "_", a)
print(b)


#camelCase -> camel_case