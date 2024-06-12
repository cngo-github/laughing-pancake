from typing import List, Union

def findLongestSubtringLength(arr: List[int]) -> Union[str, int]:
    if isinstance(arr, list) == False:
        return "N/A"
        
    n = len(arr)
    
    if(n < 2):
        return n
        
    sequences = []
    sequences.append(arr[0])
    
    for i in range(1, n):
        if arr[i] > sequences[-1]:
            sequences.append(arr[i])
        else:
            low = 0
            high = len(sequences) - 1
            
            while low < high:
                pivot = low + (high - low) // 2
                
                if sequences[pivot] < arr[i]:
                    low = pivot + 1
                else:
                    high = pivot
                    
            sequences[low] = arr[i]
            
    sequenceLength = len(sequences)
    return sequenceLength


if __name__ == "__main__":
    nums = [11,5,2,5,3,7,101,18]
    
    result = findLongestSubtringLength(nums)
    print('The length of the longest increasing substring is: %s'%(result))