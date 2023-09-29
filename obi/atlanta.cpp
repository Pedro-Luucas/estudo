#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

pair<int,int> solve(int a, int b){
    vector<pair<int,int>> poss;
    int sqB = sqrt(b)+1;
    for(int i = 1; i<sqB; i++){
        if(b % i == 0){
            int j = b / i;
            poss.push_back(make_pair(i,j));
        }
    }
    for(int i = 0; i < poss.size(); i++){
        int h, l;
        h = poss[i].first;
        l = poss[i].second;
        if(((h+1) * (l+1)) - b == a){
            return make_pair(h+1, l+1);
        }
    }
    return make_pair(-1,-1);

}


int main(){
    int a, b;
    cin >> a;
    cin >> b;
    pair<int,int> res;
    res = solve(a,b);
    cout << max(res.first, res.second) << " " << min(res.first, res.second);


}