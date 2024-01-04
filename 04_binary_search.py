from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
    return -1


print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(search(nums=[-1, 0, 3, 5, 9, 12], target=2))

# int low = 0;
#         int high = nums.length();
#         int mid;

#         while(low<=high){
#             mid = (high+low)/2;

#             if (nums[mid] == target){
#                 return mid;
#             }else if(nums[mid] > target){
#                 high = mid+1;
#             }else if(nums[mid] < target){
#                 low = mid-1;
#             }
#         }
#         return -1;
