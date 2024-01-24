#include<bits/stdc++.h>
using namespace std;

// Giả sử khóa a = 7 và khóa b = 6
static int a = 7;
static int b = 6;

string encryption(string m) {
   string c = "";
   for (int i = 0; i < m.length(); i++) {
      if(m[i]!=' ') {
        c = c + (char) ((((a * (m[i]-'A') ) + b) % 26) + 'A');
      } else {
        c += m[i];
      }
   }
   return c;
}

string decryption(string c) {
   string m = "";
   int a_inverse = 0;
   int flag = 0;
   for (int i = 0; i < 26; i++) {
      flag = (a * i) % 26;
      if (flag == 1) {
         a_inverse = i;
      }
   }
   for (int i = 0; i < c.length(); i++) {
      if(c[i] != ' ') {
        m = m + (char) (((a_inverse * ((c[i]+'A' - b)) % 26)) + 'A');
      } else {
        m += c[i];
      }
   }
   return m;
}

int main(void) {
    string msg;
    cout<<"Nhap tin nhan ban dau (VIETHOA): "; cin>>msg;
    string c = encryption(msg);
    cout << "Ma hoa tin nhan: " << c <<endl;
    cout << "Giai ma tin nhan: " << decryption(c);
    return 0;
}