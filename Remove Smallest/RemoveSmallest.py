# By Abdulrahman Mohammed Hezam / AMHezam
# https://codeforces.com/problemset/problem/1399/A

for x in range(int(input())):
	input()
	nums = list(map(int, input().split()))
	nums.sort()
	temp = len(nums)
	ans = True
	for x in range(temp):
		if len(nums) == 1:
			break
		if abs(nums[1] - nums[0]) <= 1:
			if nums[1] >= nums[0]:
				nums.pop(0)
			else:
				nums.pop(1)
		else:
			ans = False
			break
	if ans:
		print("YES")
	else:
		print("NO")
