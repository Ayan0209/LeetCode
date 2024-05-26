
            if num == target:
            mid = (start + end)//2
            num = nums[mid]
                return mid
            
            if num < target:
                start = mid + 1

            if num > target:
                end = mid - 1

        return -1        
[
