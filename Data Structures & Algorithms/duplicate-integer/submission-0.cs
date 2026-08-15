public class Solution {
    public bool hasDuplicate(int[] nums) {
        
        HashSet<int> count= new HashSet<int>();
        foreach(int n in nums)
        {
            if (count.Contains(n)) 
            {
                return true;
            }
            count.Add(n);
        }

        return false;
    }
}