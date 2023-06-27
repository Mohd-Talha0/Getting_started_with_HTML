def move_zeros(nums):
    for i in nums:
        if i == 0:
            nums.remove(i) # Remove the element from the array
            nums.append(i) # Append the element to the end
    return nums
