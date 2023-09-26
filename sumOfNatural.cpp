#include <iostream>
using namespace std;

int sum(int num){
    if (num == 1){
        return 1;
    }
    return sum(num-1) + num;
}   

int main(){
   cout << sum(10);
}
