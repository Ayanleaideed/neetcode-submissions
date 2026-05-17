class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        # check each number if the on the hashmap 
        for n in nums:
            if n in hashMap:
                hashMap[n] += 1 
            else:
                hashMap[n] = 1 
        
        # return sorted(list(hashMap.values()), reverse=True)[:k]
        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        return [num for num, count in sorted_items[:k]]