#include <iostream>
#include <sstream>
#include <set>
using std::cout;
using std::endl;

bool is_palindrome(const std::string &str) {
    std::string::const_iterator direct=str.begin();
    std::string::const_reverse_iterator reverse=str.rbegin();

    while (direct!=str.end()) {
        if (*direct!=*reverse) return false;
        direct++;
        reverse++;
    }
    return true;
}

int main() {
    std::set<int> results;
    for (int k=1; k<1000; k++) for (int l=1; l<1000; l++) {
        std::stringstream ss;
        ss<<l*k;
        if (is_palindrome(ss.str())) results.insert(l*k);
    }
    cout<<*results.rbegin()<<endl;
}
