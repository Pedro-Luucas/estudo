#include <iostream>
using namespace std;

string binario(int dec, string binar = ""){
    if(dec == 0){
        return binar;
    }
    string strr = to_string(dec % 2);
    binar = strr + binar
    return binario(dec / 2 , binar);
}

int main(){
   cout << binario(127);
}
