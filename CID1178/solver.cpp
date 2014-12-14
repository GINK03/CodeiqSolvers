#include<list>
#include<vector>
#include<iostream>
#include<map>
#include<random>
#include<unordered_map>
#include<algorithm>
using namespace std;
int main(){
  vector<vector<int>> base = {
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0, 1},
    {1, 1, 0, 0, 0},
    {0, 0, 0, 1, 0},
    {1, 1, 0, 0, 0},
  }; 
  unordered_map<int, pair<int, int>> h = {
    {1, {2, -1}},
    {2, {1, 2}},
    {3, {-1, 2}},
    {4, {1, -2}},
    {5, {-1, -2}},
    {6, {-2, 1}},
    {7, {-2, -1}},
  }; 
  while(true){
    vector<int> p = {0, 0};
    auto copybase = base;
    auto count = 0;
    vector<pair<int, int>> trace;
    while(true){
      auto deadend = 0;
      while(true){
        auto output = 0 + (rand()%(int)(8 - 0 + 1));
        auto &href  = h[int(output)];
        vector<int> ptmp   = {p[0] - href.first, p[1] - href.second};
        if(ptmp[0] >= 0 and ptmp[1] >= 0 and ptmp[0] < 5 and ptmp[1] < 5 and copybase[ptmp[0]][ptmp[1]] > 0){
          copybase[ptmp[0]][ptmp[1]] = -1;
          count += 1;
          p = ptmp;
          trace.push_back({ptmp[0], ptmp[1]});
          break;
        }
        if(ptmp[0] >= 0 and ptmp[1] >= 0 and ptmp[0] < 5 and ptmp[1] < 5 and copybase[ptmp[0]][ptmp[1]] < 0){
          deadend += 1;
          if(deadend > 100000)
            break;
        }
      }
      if(deadend > 100000)
        break;
    }
    vector<int> res;
    for(auto cb: copybase){
      for(auto e: cb){
        //cout << e << " ";
        res.push_back(e);
      }
    }
    auto out = count_if(res.begin(), res.end(), [](int x){ return x == 1;});
    if( out == 0 ){
      cout << "iter, ";
      for(auto o : res) cout << o;
      for(auto t: trace) cout << "[" << t.first << "," << t.second << "]";
      cout << " 1num" << out << " count" << count << endl;
    }
  }
}
