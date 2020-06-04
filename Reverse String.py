class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ls = len(s)
        ls2 = (ls>>1) +(0 if ls%2==0 else 1)
        print(ls2)

        left=0
        right=len(s)-1
        
        for i in range(ls2):
            temp = s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        return s
            
