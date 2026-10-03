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

  private static final int[][] DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

  private void bfs(char[][] grid, int r, int c) {
    Queue<Pair<Integer, Integer>> q = new ArrayDeque<>(List.of(new Pair<>(r, c)));
  
