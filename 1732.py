class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = -100 
        visota = 0
        for j in range(len(gain)):
            visota = visota + gain[j]
            if height < visota:
                height = visota
                        
        return height  