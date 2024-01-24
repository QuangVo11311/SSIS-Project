#include <iostream>
using namespace std;

// Hàm tính gcd(a, b) bằng thuật toán Euclidean
int gcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    
    x = y1;
    y = x1 - (a / b) * y1;
    
    return d;
}

int main() {
    int a, b;
    cout << "Nhap a: ";
    cin >> a;
    cout << "Nhap b: ";
    cin >> b;
    
    int x, y, d;
    d = gcd(a, b, x, y);
    
    cout << "GCD(" << a << ", " << b << ") = " << d << endl;
    cout << "x = " << x << ", y = " << y << endl;
    
    return 0;
}
