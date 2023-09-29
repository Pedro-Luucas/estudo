#include <iostream>
using namespace std;

bool palind(string strr){
    
    if(strr.length() == 0 || strr.length() == 1){
        return true;
    }
    if(strr.at(0) == strr.at(strr.length() - 1)){
        return(palind(strr.substr(1,strr.length() - 2)));
    }
    else{
        return false;
    }
}

int main(){
   cout << palind("abasaba");
}
