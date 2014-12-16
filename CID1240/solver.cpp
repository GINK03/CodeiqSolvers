#include<iostream>
#include<list>
#include<algorithm>
#include<string>
using namespace std;

list<int> s = {1,2,3,4,5,6,7,8,9,10,11,12};
const list<int> cs = {1,2,3,4,5,6,7,8,9,10,11,12};
int main(){
  auto result = 0;
  do{
    list<pair<int, int>> evallist;
    auto sit = --s.begin();
    auto csit = --cs.begin();
    for(auto i = 0; i<12; ++i){
      evallist.push_back(pair<int,int>(*(++sit),
                                    *(++csit)));
    }
    evallist.remove_if([](pair<int,int> x){
        return x.first == x.second;
    });
    if(evallist.size() == 12){
      result++;
    }
  }while(next_permutation(s.begin(), s.end()));
  cout << "result, " << result << endl; 
}

