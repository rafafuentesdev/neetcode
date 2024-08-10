# Problem: Duplicate Integer

[NeetCode]([https://neetcode.io](https://neetcode.io/problems/duplicate-integer))

### Problem Statement

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

### Examples

Example 1:

```python
Input: nums = [1, 2, 3, 3]

Output: true
```

Example 2:

```python
Input: nums = [1, 2, 3, 4]

Output: false
```

## Approach 1: Brute Force

### Intuition

Compare each number with every other number in the array that comes after it.

### Algorithm

1. Iterate through the array with index i from 0 to length-2.
2. For each i, iterate with index j from i+1 to length-1.
3. If nums[i] equals nums[j], return true (duplicate found).
4. If no duplicates are found after all comparisons, return false.

### Complexity Analysis

- Time complexity: O(n^2), where n is the length of the array. In the worst case, we compare each element with every other element that comes after it.
- Space complexity: O(1), as we only use a constant amount of extra space.

## Key Takeaways

- To compare each pair efficiently, we don't need to compare every element with every other element:
  - We can start the inner loop from i+1 for each outer loop iteration.
  - This avoids unnecessary comparisons and ensures we don't compare an element with itself or repeat comparisons.

### Code

```python
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False
```

## Approach 2: Sorting

### Intuition

By sorting the array first, any duplicate elements will become adjacent to each other. This allows us to check for duplicates in a single pass through the sorted array.

Example:
Input: nums = [1, 2, 3, 1]
Sorted Input: nums = [1, 1, 2, 3]

### Algorithm

1. Sort the input array.
2. Iterate through the sorted array once, comparing each element with its next neighbor.
3. If any two adjacent elements are equal, return True (duplicate found).
4. If we complete the iteration without finding duplicates, return False.

### Complexity Analysis

- Time complexity: O(n log n), where n is the length of the array.
  - Sorting typically takes O(n log n) time.
  - The subsequent linear scan takes O(n) time.
  - The overall time complexity is dominated by the sorting step: O(n log n) + O(n) = O(n log n)
- Space complexity:
  - O(1) if we use an in-place sorting algorithm and don't count the space used by sorting.
  - O(n) if we consider the space used by some sorting algorithms (e.g., Merge Sort).

### Code

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort() # Sort the array in-place
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
```

## Key Takeaways

1. Sorting can simplify certain problems by bringing related elements together.
2. This approach trades off increased time complexity (due to sorting) for simplified logic and reduced space complexity compared to other methods (like using a hash set).
3. The choice between this method and others (like hash set) depends on factors such as the size of the input, memory constraints, and whether preserving the original order is important.

## Approach 3: Most Optimal Solution Using HashSet

### Intuition

A HashSet provides constant-time O(1) operations for both insertion and lookup. By using a HashSet, we can efficiently track unique elements and quickly identify duplicates.

### Algorithm

1. Initialize an empty HashSet.
2. Iterate through each element in the input array:
   a. If the current element is already in the HashSet, we've found a duplicate, so return True.
   b. If not, add the current element to the HashSet.
3. If we complete the iteration without finding duplicates, return False.

### Complexity Analysis

- Time complexity: O(n), where n is the length of the input array.
  - We perform a single pass through the array.
  - HashSet operations (insertion and lookup) are O(1) on average.
- Space complexity: O(n) in the worst case.
  - In the worst case (no duplicates), we store all n elements in the HashSet.
  - In the best case (duplicate found immediately), it's O(1).

### Code

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

### Key Takeaways

1. HashSet provides an optimal balance of time and space efficiency for this problem.
2. This approach is generally preferable to sorting when:
   - We don't need to preserve the original order of elements.
   - We prioritize time complexity over space complexity.
3. The HashSet approach is particularly efficient for large datasets or when quick lookup is crucial.
4. In Python, using a set is more idiomatic and slightly more efficient than using a dict for this purpose.

### Trade-offs

- Compared to the sorting approach:

  - Better time complexity: O(n) vs O(n log n)
  - Worse space complexity in most cases: O(n) vs O(1) for in-place sorting

- Compared to the brute force approach:
  - Much better time complexity: O(n) vs O(n^2)
  - Worse space complexity: O(n) vs O(1)

### Python-specific Note

In Python, we could solve this even more concisely using the built-in set:

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```

This one-liner creates a set from the input list, which automatically removes duplicates. If the length of this set is different from the original list, it means there were duplicates.

## Quiz

1. How many possible pairs of elements are there in an array of size n?

Solution: n^2

There are exactly n \* (n - 1) / 2 distinct pairs of integers in the array. This is equivalent to (n^2 - n) / 2, and we normally consider the largest term, which in this case is n^2.

2. What is the time complexity of a brute force approach, where you compare every possible pair in the array to check if there are any duplicates?

Solution: O(n^2)

The brute-force solution using two nested loops has a time complexity of O(n^2) because for each element in the array, you need to iterate over up to n other elements.

3. What data structure can you use to optimize the approach for checking if there are any duplicate elements in the array?

Solution: HashMap or HashSet

A Hashmap (or Hashtable) and a HashSet allow us to store and retrieve values in constant time, O(1). We can utilize this property to efficiently check for duplicates.

4. How can a HashSet be used to efficiently check for duplicates in the array?

A HashSet does not allow duplicate values. So, if you try to insert an element that already exists in the HashSet, it will not add the element and you know you've found a duplicate (choice A). Alternatively, you could add all elements to the HashSet and then compare its size to the size of the array. If the sizes are different, then there must have been a duplicate in the array (choice B). Both these methods will help identify if a duplicate exists in the array.

5. What is the time and space complexity of the solution using a hashmap?

Time Complexity -> O(n)
Space Complexity -> O(n)

The hashmap solution has a time complexity of O(n) because you need to iterate through the array once. Also, the key lookup operation with hashmaps runs in O(1) time. The space complexity is also O(n) because, in the worst case, you might need to store all n elements in the hashmap.
