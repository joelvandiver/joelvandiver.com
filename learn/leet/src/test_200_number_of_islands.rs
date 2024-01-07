struct Solution;

fn dfs(grid: &mut Vec<Vec<char>>, i: isize, j: isize) {
    if i < 0 || j < 0 || i >= grid.len() as isize || j >= grid[0].len() as isize {
        return;
    }
    if grid[i as usize][j as usize] == '0' {
        return;
    }
    if grid[i as usize][j as usize] == '1' {
        grid[i as usize][j as usize] = '0';
    }

    dfs(grid, i + 1, j);
    dfs(grid, i - 1, j);
    dfs(grid, i, j + 1);
    dfs(grid, i, j - 1);
}

impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let mut count = 0;

        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                if grid[i][j] == '1' {
                    count += 1;
                    dfs(&mut grid, i as isize, j as isize);
                }
            }
        }

        count
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex_1() {
        let grid = vec![
            vec!['1', '1', '1', '1', '0'],
            vec!['1', '1', '0', '1', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '0', '0', '0'],
        ];

        assert_eq!(Solution::num_islands(grid), 1);
    }

    #[test]
    fn test_ex_2() {
        let grid = vec![
            vec!['1', '1', '0', '0', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '1', '0', '0'],
            vec!['0', '0', '0', '1', '1'],
        ];

        assert_eq!(Solution::num_islands(grid), 3);
    }
}
