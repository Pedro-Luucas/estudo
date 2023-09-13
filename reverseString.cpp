#include <iostream>
using namespace std;

string reverse(string strr){
    if(strr == ""){
        return "";
    }
    return reverse((strr.substr(1))) + (strr.substr(0,1));
}


int main(){
   cout << reverse("pedrao");
}
