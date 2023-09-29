#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// MAXIMUM DISTANCE 
int distance(int x1, int y1, int x2, int y2){
    int p1 = x1 - x2;
    int p2 = y1 - y2;
    return (pow(p1, 2) + pow(p2, 2));
}

int main(){
    int max = 0;
    int n;
    cin >> n;
    vector<int> x(n), y(n);
    for(int i=0; i<n; i++){
        cin >> x[i];
    }
    for(int i=0; i<n; i++){
        cin >> y[i];
    }

    for(int i=0; i<n; i++){
        for(int j=i; j<n; j++){
            int res = distance(x[i], y[i], x[j], y[j]);
            if(res > max){
                max = res;
            }
        }
    }
    cout << max;

    return 0;
}