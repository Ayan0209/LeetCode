            if sorted_nums[i+1] < curr_num:
                remaining_val = len(sorted_nums) - (i+1)
                dict[curr_num] = remaining_val
        
        dict[sorted_nums[-1]] = 0

        result = []
        for num in nums:
            result.append(dict[num])

        return result

[
