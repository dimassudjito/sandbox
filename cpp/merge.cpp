#include <iostream>
using namespace std;

/*
> Input:
- nums1: array of int, length m+n, non-decreasing
- nums2: array of int, length of n, non-decreasing
- m: # valid int in nums1
- n: # valid int in nums2
> Output
- nums1: modified version
> process
- by merging nums1 and nums2
> assumption:
- 0 padding is always put at the end
---
> example
- see prompt
---
> method 1: by creating new array and merging it manually 
- time-compelxity: o(2m+n), space-complexity: (2m)
1. cache nums1 real content to another array num3
2. iterate nums2 and nums3:
3. put the smaller number in nums1, give priority to nums3 (arbitrary)
4. move pointer to array when adding from that array
*/
void merge(int nums1[], int m, int nums2[], int n);

int main() {
  int nums1[] = {1, 2, 3, 0, 0, 0};
  int nums2[] = {2, 5, 6};
  int nums1Length = sizeof(nums1)/sizeof(*nums1);
  int n = sizeof(nums2)/sizeof(*nums2);
  int m = nums1Length - n;
  merge(nums1, m, nums2, n);
  // DEBUG
  cout << "---" << endl;
  for (int i=0; i<m+n; i++) {
    cout << nums1[i] << endl;
  }
  return 0;
}

void merge(int nums1[], int m, int nums2[], int n) {
  // cache nums1
  int nums3[m];
  for (int i=0; i<m; i++) {
    nums3[i] = nums1[i];
  }

  /*
  for (int i=0; i<m; i++) {
    cout << nums3[i] << endl;
  }
  for (int i=0; i<n; i++) {
    cout << nums2[i] << endl;
  }
  */
  
  // start merging until one of them runs out
  int p1 = 0, p2 = 0, p3 = 0; // pointers to nums1, nums2, nums3
  while (p2 < n &&  p3 < m) {
    // check what's smaller
    if (nums2[p2] <= nums3[p3]) {
      // add nums2 it to nums1
      nums1[p1] = nums2[p2];
      // increment pointer
      p1++;
      p2++;
    } else {
      // add nums3 to nums1
      nums1[p1] = nums3[p3];
      // increment pointer
      p1++;
      p3++;
    }
  }
  // add the rest
  if (p2 == n) {
    // nums2 run out, add the rest of nums3
    while (p3 < m) {
      nums1[p1] = nums3[p3];
      p1++;
      p3++;
    }
  } else {
    // nums3 run out, add the rest of nums2
    while (p2 < n) {
      nums1[p1] = nums2[p2];
      p1++;
      p2++;
    }
  }
}
