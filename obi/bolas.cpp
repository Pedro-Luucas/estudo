#include<iostream>
using namespace std;

// 

int main()
{
    int bolas[8];
    int nums[10] = {0,0,0,0,0,0,0,0,0,0};

    for(int i=0;i<8;i++)
    {
        cin>>bolas[i];
        nums[bolas[i]]++;
    }
    for(int i;i<10;i++)
    {
        if(nums[i] >= 4)
        {
            cout << "N";
            return 0;
        }
    }
    cout << "S";
    return 0;
}