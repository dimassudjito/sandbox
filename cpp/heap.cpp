#include <iostream>
using namespace std;

int createArr();

int main() {
  createArr();
  return 0;
}

int createArr() {
  int n;
  cin >> n;
  int arr[n];
  for (int i=0; i<n; i++) {
    arr[i] = 5;
  }
  return 0;
}
