# https://www.acmicpc.net/problem/10815

from sys import stdin
x=stdin.readline
x()
c=set(x().strip().split())
x()
l=list(x().strip().split())
for i in l:print(1 if i in c else 0,end=' ')