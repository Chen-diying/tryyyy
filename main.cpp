#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> mystack;
    int input, n;
    cin >> input >> n;
    if((input == 0)){
        cout << 0;
        return 1;
    }
    if(n < 2 && n > 10)
        return 1;
    for(int i = 0, t = input; t > 0; i++){
        mystack.push(t%n);
        t /= n;
    }
    while (!mystack.empty()){
        int top = mystack.top();
        mystack.pop();
        cout << top;
    }

    return 0;
}