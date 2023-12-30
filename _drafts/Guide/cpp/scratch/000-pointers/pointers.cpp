// Citation for the following code:
// Title: "C++ Pointers" [Online Tutorial]. Geeks for Geeks
// Accessed Date: 5/20/2023
// Description: This is a simple program to demonstrate the use of pointers.
// Source URL: https://www.geeksforgeeks.org/cpp-pointers/

// C++ program to illustrate Pointers

#include <bits/stdc++.h>
using namespace std;
void geeks()
{
    int var = 20;

    // declare pointer variable
    int* ptr = &var;

    // assign the address of a variable to a pointer
    cout << "Value at ptr = " << ptr << "\n";    
    cout << "Value at var = " << var << "\n";    
    cout << "Value at *ptr = " << *ptr << "\n";    
}
// Driver program
int main()
{
    geeks();
    return 0;
}

/** Output
Value at ptr = 0x7fffffffe024
Value at var = 20
Value at *ptr = 20
*/

// TODO:  Continue -> References and Pointers