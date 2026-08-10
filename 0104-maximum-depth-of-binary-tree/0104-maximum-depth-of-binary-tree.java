/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans;
    public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        ans = 0;
        dfs(root,1);
        return ans;
    }
    public void dfs(TreeNode root, int dep){
        if(root.left != null){
            ans=Math.max(dep,ans);
            dfs(root.left,dep+1);
        }
        if(root.right != null){
            ans=Math.max(dep,ans);
            dfs(root.right,dep+1);
        }
        ans = Math.max(ans,dep);
        return;
    }
}