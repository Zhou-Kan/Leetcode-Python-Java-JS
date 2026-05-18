#include<iostream>
using namespace std;
int mySqrt(int x) {
    int left = 0, right = x / 2 + 1;
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        if (mid > x / mid) {
            right = mid - 1;
        } else {
            left = mid;
        }
    }
    return left;
}

int main() {

    cout << mySqrt(2) << endl;
    cout << mySqrt(8) << endl;
    cout << mySqrt(0) << endl; 
    return 0;
}