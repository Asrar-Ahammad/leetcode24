#include <bits/stdc++.h>
using namespace std;

int numberOfBeams(vector<string> &bank)
{
    int prev = 0, curr = 0, count = 0;
    for (auto i : bank)
    {
        for (auto j : i)
        {
            if (j == '1')
            {
                curr++;
            }
        }
        if (curr == 0)
        {
            continue;
        }
        count = count + (curr * prev);
        prev = curr;
        curr = 0;
    }
    return count;
}

int main()
{
    vector<string> bank;
    bank = {"011001", "000000", "010100", "001000"};
    cout << numberOfBeams(bank);
    int _w = 0;

    return 0;
}
