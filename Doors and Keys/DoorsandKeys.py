# https://codeforces.com/problemset/problem/1644/A

def innerLoop():
	ans = {0}
	for letter in keys:
		if letter.islower():
			ans.add(letter)
			continue
		elif letter == "R":
			if "r" not in ans:
				return "NO"
		elif letter == "G":
			if "g" not in ans:
				return "NO"
		else:
			if "b" not in ans:
				return "NO"
	return "YES"


for x in range(int(input())):
	keys = input()
	print(innerLoop())
