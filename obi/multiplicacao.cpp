#include <iostream>
using namespace std;

int mult(int x, int y){
    if(y > x){
        return(mult(y, x));
    }
    else if (y != 0){
        return (x + mult(x, y - 1));
    }
    else {
        return 0
    }
}   

int main(){
   cout << mult(10,10);
}
