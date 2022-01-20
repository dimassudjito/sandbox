#include <iostream>
using namespace std;

int removeElement(int nums[], int length, int val);

int main() {
  int nums[4] =  {3, 2, 2, 3};
  int res = removeElement(nums, sizeof(nums)/sizeof(*nums), 3);
  // DEBUG: print result
  cout << "k = " << res << endl;
  for (int i=0; i < 4; i++) {
    cout << nums[i] << endl;
  }
  
  return 0;
}

/*
> Method 1: brute force
- O(n^2)
1. iterate the array, every time it found target, move the rest of the element 1 step
2. set counter to keep track how many values need to be replaced in the end
3. replace the value in the end with _
- problem: if next element is also target
*/
int removeElement(int nums[], int length, int val) {
  for (int i=0; i<length; i++) {
    if (nums[i] == val) {
      // move back the rest of the of element
      for (int j=i; j<length-1; j++) {
	nums[j] = nums[j+1];
      }
    }
  }
  return val;
}
