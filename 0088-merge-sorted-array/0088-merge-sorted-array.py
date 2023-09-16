class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return nums1
        
        one_pointer = m-1
        two_pointer = n-1
        
        current = len(nums1)-1
        while two_pointer >= 0:
            if one_pointer >= 0 and nums1[one_pointer] > nums2[two_pointer]:
                nums1[current] = nums1[one_pointer]
                one_pointer -= 1
            else:
                nums1[current] = nums2[two_pointer]
                two_pointer -= 1
            current -= 1
            
        
        