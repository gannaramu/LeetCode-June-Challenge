class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pass method
#         new=[0, 0, 0]
#         for i in nums:
#             new[i]=new[i]+1
#             print(new)
#         a=0
#         j=0
#         result=[]
#         for i in new:
#             for k in range(i):
#                 nums[j]=a
#                 print(nums)
#                 j=j+1
#             a+=1
            
        
#         return 

# one pass algorithm
        left =0
        right=len(nums)-1
        mid=0
        if right==0:
            return nums
        for q in range(len(nums)):
            if left>=len(nums)-1:
                break
            if right<=0:
                break
            if mid>right:
                break
                           
            if nums[mid]==0:
                temp = nums[left]
                nums[left]=nums[mid]
                nums[mid]=temp
                left=left+1
                mid=mid+1
                
            elif nums[mid]==2:
                temp = nums[right]
                nums[right]=nums[mid]
                nums[mid]=temp
                right=right-1
                
            elif nums[mid]==1:
                mid=mid+1
        
