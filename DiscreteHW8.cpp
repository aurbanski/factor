#include <iostream>
#include <cstdlib>
#include <math.h>
using namespace std;

int findOneFactorint(unsigned long long int n);
int main()
{
    unsigned long long int num;
    cout << "Number you want to factor: ";
    cin >> num;
    findOneFactorint(num);
    return 0;
}

int findOneFactorint(unsigned long long int n)
{
    unsigned long long int arr[n-1];
    for (unsigned long long int i=0; i<n+1; i++)
    {
        arr[i] = i;
    }

    for (unsigned long long int j=2; j*j<n+1; j++)
    {
        for (unsigned long long int k=2; j*k<n+1; k++)
        {
            if (arr[(j*k)] != 0)//because the value in arr[j] = j
                arr[j*k] = 0;
        }
    }

    unsigned long long int primeArray[(n+1)/4];
    for (unsigned long long int pri = 0; pri < (n+1)/4; pri++)
    {
        primeArray[pri] = 0;
    }
    int b=0;
    for (unsigned long long int a=0; a<n+1; a++)
    {
        if (arr[a] != 0 && arr[a] != 1)
        {
            cout << arr[a]<< endl;
            primeArray[b] = arr[a];
            cout << b << "th prime factors: " << primeArray[b] << endl;
            b++;
        }

    }

    /*for (long long int c = 0; c < n/2; c++)
    {
        bool flag = false;
        if (n % primeArray[c] == 0)
        {
            cout << primeArray[c] << endl;
            long long int m = n/primeArray[c];
            for (long long int d=0; d<n/4; d++)
            {
                if (primeArray[d] == m)
                {
                    flag = true;
                }
            }
            if (flag == true)
            {
                cout << "p = " << primeArray[c] << endl;
                cout << "q = " << m << endl;
            }
        }
    }*/

}
