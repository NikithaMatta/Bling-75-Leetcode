import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        for (int num : nums) {
            if (!set.add(num)) { // If add() returns false, it means num is already in the set
                return true;
            }
        }
        
        return false;
    }
}
