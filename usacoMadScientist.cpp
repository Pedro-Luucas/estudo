#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    int min = 0;
    bool miss = false;
    cin >> n;
    string a,b;
    cin >> a;
    cin >> b;

    for (int i = 0; i < n; i++){
        if(a[i] == b[i]){
            if(!miss){
                min += 1;
            }
            miss = true;
        }
        else{
            miss = false;
        }
    }


    cout << min;
}