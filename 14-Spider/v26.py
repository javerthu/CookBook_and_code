'''
findall案例
加贪婪匹配的机制
'''
import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 years odl and 185 high")

print(s)

s = pattern.finditer("i am 18 years odl and 185 high")

print(type(s))

for i in s:
    print(i.group())

p = re.compile(r'.*?w')

s = p.findall("awbwccwdwvw123w")

print(s)

s = p.finditer("awbwccwdwvw123w")

print(type(s))

for i in s:
    print(i.group())