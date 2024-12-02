from utils import aoc

data = aoc.get_data_for(day=1)
print(data)

distances_sum = 0
nums1, nums2 = [], []

for row in data:
    num1, num2 = row.split()
    nums1.append(int(num1))
    nums2.append(int(num2))

nums1.sort()
nums2.sort()

for i in range(len(nums1)):
    distances_sum += abs(nums1[i] - nums2[i])

print(distances_sum)