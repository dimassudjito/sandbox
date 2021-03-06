#include <iostream>
using namespace std;

int MAX = 46;

int climbStairs(int n);

int main() {
  int res = climbStairs(5);
  cout << "res: " << res << endl;
  return 0;
}

/*
> Input: int n numbers of steps to get to the top of the stairs
> output: numbers of ways you can take the stairs
> process: count permutation of possible steps (1 and 2)
> assumption:
- n between 1 to 45
---
example
> n=2 -> 2 ([1,1] [2])
> n=3 -> 3 ([1,1,1] [1,2] [2,1])
> n=4 -> 5
> n=5 -> 8
> n=6 -> 13
---
> method 1: memoization
- time-complexity: O(N)
1. starts with [1, 1]
2. combine adjacent steps until nth steps
*/
int climbStairs(int n) {
  // init array
  int ways[MAX] = {1, 1};
  for (int i=2; i<=n; i++) {
    ways[i] = ways[i-1] + ways[i-2];
  }
  return ways[n];
  
}
