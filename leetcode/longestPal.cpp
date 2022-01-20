#include <iostream>
#include <string>

using namespace std;

string palindrome(string s) {
    string o = s.substr(0, 1); // at least 1st letter is palindrome

    for (int i = 0; i < s.length(); ++i) {
        // test pivot
        if (i-1 >= 0 && i+1 < s.length() && s[i-1] == s[i+1]) {     
            // SINGLE_PIVOT
            if (o.length() < 3) {o = s.substr(i-1, 3);}
            for (int j = 2; j < s.length(); ++j) {
                if (i-j >=0 && i+j < s.length() && s[i-j] == s[i+j]) {
                    if (o.length() < 2*j+1) {o = s.substr(i-j, 2*j+1);}
                } else {break;} 
            }     
        } 
        if (i-1 > 0 && s[i-1] == s[i]) {
            // DOUBLE_PIVOT
            if (o.length() < 2) {o = s.substr(i-1, 2);}
            for (int j = 1; j < s.length(); ++j) {
                if (i-j-1 >= 0 && i+j < s.length() && s[i-j-1] == s[i+j]) {
                    if (o.length() < (j+1)*2) {o = s.substr(i-j-1, (j+1)*2);}
                } else {break;}
            }
        }
        if (i+1 < s.length() && s[i+1] == s[i]) {
            // DOUBLE_PIVOT
            if (o.length() < 2) {o = s.substr(i, 2);}
            for (int j = 1; j < s.length(); ++j) {
                if (i-j >= 0 && i+j+1 < s.length() && s[i-j] == s[i+j+1]) {
                    if (o.length() < (j+1)*2) {o = s.substr(i-j, (j+1)*2);}
                } else {break;}
            }
        } else {continue;}
    }

    return o;
}

int main() {
    string word;
    cin >> word;
    cout << palindrome(word) << endl;

    return 0;
}