                int remainingVal = i;
                dict.put(currNum, remainingVal);
        for (int i = sortedNums.length - 1; i > 0; i--) {
            int currNum = sortedNums[i];
            if (sortedNums[i - 1] < currNum) {
        Arrays.sort(sortedNums);

        Map<Integer, Integer> dict = new HashMap<>();
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] sortedNums = nums.clone();
[
