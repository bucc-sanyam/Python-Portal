def moveZeros(nums):
    """
    Given a list, modify nums in-place by moving zeroes to the end.
    Complexity: O(n)
    """
    non_zero_pointer = 0
    temp = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[non_zero_pointer]
            nums[non_zero_pointer] = nums[i]
            nums[i] = temp
            non_zero_pointer += 1
    print("Moved zeros to the end: ", nums)

def largestNumber(nums):
    """
    Given a list of non-sorted positive integers, find the largest number.
    Complexity: O(n)
    """
    largest = 0
    for i in nums:
        if(i > largest):
            largest = i
    print("Largest Integer in the array: ", largest)

def secondLargestNumber(nums):
    """
    Given a list of non-sorted positive integers, find the second-largest number,
    returns -1 if there's no second largest.
    Complexity: O(n)
    """
    second_largest = -1
    largest = -1
    for i in nums:
        if(i > largest):
            second_largest = largest
            largest = i
        elif(i > second_largest and i != largest):
            second_largest = i
    print("Second Largest Integer in the array: ", second_largest)

def reverseArray(nums):
    """
    Given an array of integers, reverse the array.
    Complexity: O(n)
    """
    start = 0
    end = len(nums) - 1
    while(start < end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
    print("Reversed Array: ", nums)

def leftRotateArray(nums):
    """
    Given an array of integers, rotate the elements of the array to the left.
    Complexity: O(n)
    """
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]
    nums[len(nums)-1] = temp
    print("Left Rotated Array: ", nums)

if __name__ == "__main__":
    original_array = [0, 17, 0, 3, 12, 20, 15]
    # Shallow copy of the input array
    input_array = original_array.copy()
    print("Input Array: ", input_array)
    print("-"*50)
    moveZeros(input_array.copy())
    print("-"*50)
    largestNumber(input_array)
    print("-"*50)
    secondLargestNumber(input_array)
    print("-"*50)
    reverseArray(input_array)
    print("-"*50)
    leftRotateArray(input_array)
    print("-"*50)