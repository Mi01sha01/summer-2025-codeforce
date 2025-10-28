#include <bits/stdc++.h>
using namespace std;

int main()
{
  int t;
  cin >> t;
  while(t--)
  {
    long long x;
    cin >> x;
    if (x==9)
      cout << 1 << endl;
    else if (x < 9) 
      cout << 0 << endl;
      
    else if (x%10==9)
      cout << x/10 +1 << endl;
      
    else
      cout << x/10<< endl;  
        
  }
  return 0;
}