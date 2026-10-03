class Solution {
  public int numIslands(char[][] grid) {
    int ans = 0;

    for (int i = 0; i < grid.length; ++i)
      for (int j = 0; j < grid[0].length; ++j)
        if (grid[i][j] == '1') {
          bfs(grid, i, j);
          ++ans;
        }

    return ans;
  }

