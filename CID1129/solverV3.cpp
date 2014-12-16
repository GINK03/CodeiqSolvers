#include<set>
#include<iostream>
#include<vector>
#include<map>
using namespace std;

vector<long> inputs = {
12434,
657751,
151251,
805211,
1755178,
1767886,
27720560,
40259059
};
map<long, long long> m;

long long fibonacci(long n){
  //if( m.find(n) != m.end() ) 
  //  return m.find(n)->second;
  long long a = 0;
  long long b = 1;
  for(long i = 0; i < n ; i++){
    auto temp = b;
    b = a+temp;
    a = temp;
  }
  m.insert(pair<long, long long>(n, a));
  return a;
}

long long resolve_fibonacci(long n){
  if(n <= 100000000){
    return fibonacci(n);
  }
  /*if( n%2 == 1){
    return resolve_fibonacci( (n-1)/2 + 1 )*resolve_fibonacci( (n-1)/2 + 1 ) + resolve_fibonacci( (n-1)/2 )*resolve_fibonacci( (n-1)/2 );
  }else{
    return resolve_fibonacci( n/2 )*( 2*resolve_fibonacci(n/2 + 1) - resolve_fibonacci(n/2));
  }*/
}
int main(){
  for(auto i : inputs){
    long long result = resolve_fibonacci(i);
    cout << "inputs," << i << " fib," << result << endl;
  }
}
