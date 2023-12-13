'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0
        l,r = 0,len(height)-1
        lMax,rMax = height[l],height[r]    
        res=0

        while l < r :
            if lMax < rMax :
                l+=1
                lMax=max(lMax,height[l])
                res+=lMax-height[l]
            else:
                r-=1
                rMax=max(rMax,height[r])
                res+=rMax-height[r]
        return res        
