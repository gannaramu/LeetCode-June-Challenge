class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left=0
        right=len(nums)-1
        
        print(left,right)
        a=1
        while a:
            if nums[(right+left)>>1] ==target:
                a=0 
                return (right+left)>>1
            elif right-left<=1:
                if target>nums[right]:
                    return right+1
                elif target<nums[left]:
                    return left
                else:
                    return right
                
            elif nums[(right+left)>>1] <=target:
                left = (right+left)>>1
        
            elif nums[(right+left)>>1] >=target:
                right = (right+left)>>1
            
          
            
                
            print(left,right)
        
