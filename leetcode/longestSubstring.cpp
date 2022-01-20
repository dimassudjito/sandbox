#include <unordered_map>
#include <iostream>

using namespace std;

int lengthOfLongestSubstring(string s) {    
    unordered_map<char, int> tracker;
    int counter = 0, max = 0, last_copied=-99;
    
    for (int i=0; i<s.length(); ++i) {
        if (tracker.find(s[i]) == tracker.end()){
            tracker[s[i]] = i; // get original occurence
            counter++;
        } else {      
            if (tracker[s[i]] < last_copied) { // original is before last copied
                counter++; 
                tracker[s[i]] = i; // update tracker
                continue;
            }
            
            if (counter > max) {max = counter;}
            
            counter = i-tracker[s[i]]; // reset counter
            last_copied = tracker[s[i]]; // update last_copied
            tracker[s[i]] = i; // update tracker
        }
    }
    if (counter > max) {max = counter;}

    
    return max;
}

int main() {
    cout << lengthOfLongestSubstring("aabaab!bb") << endl;
    return 0;
}
