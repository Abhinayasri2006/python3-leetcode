class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < n:
            result.append(nums1[i])
            i += 1
        while j < m:
            result.append(nums2[j])
            j += 1
        l = len(result)
        if l % 2 == 0:
            return (result[l // 2 - 1] + result[l // 2]) / 2
        return result[l // 2]
        
        