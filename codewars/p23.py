class Solution:
    def subarraySum(self, arr, target):
        while i<len(arr):
            if arr[i]+arr[j]==target:
                return 