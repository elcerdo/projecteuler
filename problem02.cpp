#include <iostream>
using std::cout;
using std::endl;

int main() {
    long sum=2;
    long oo=1;
    long o=2;
    long n=3;
    while (n<=4e6) {
        if (n%2==0) sum+=n;
        oo=o;
        o=n;

        n=o+oo;
    }

    cout<<sum<<endl;
}
