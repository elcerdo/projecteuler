#include <iostream>
using std::cout;
using std::endl;

int main() {
    long sum=0;
    for (long k=0; k<1000; k++) if (k%3==0 or k%5==0) sum+=k;
    cout<<sum<<endl;
}
