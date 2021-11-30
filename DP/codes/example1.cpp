#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
typedef long long int ll;
#define pll pair<ll, ll>
#define pii pair<int, int>
#define fo(i,n) for(int i=0;i<n;i++)
#define foi(i, n) for (int i = n - 1; i >= 0; i--)
long long int M = 1e9 + 7;
#define vi vector<int>
#define vpi vector<pair<int,int>
#define number_of_balls 121 // 0 - 120 need both for dp state so that is why 121
#define number_of_wickets 11 // 0 -10
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    double dp[number_of_balls][number_of_wickets];
    fo(i,number_of_balls)
    {
        dp[i][0]=0;
    }
    fo(i,number_of_wickets)
    {
        dp[0][i]=0;
    }
    for(int i=1;i<number_of_balls;i++)
    {
        for(int j=1;j<number_of_wickets;j++)
        {
            dp[i][j]= (0.05*(dp[i-1][j-1])) + (0.95*(dp[i-1][j])) + (1.3388) ;
        }
    }
    cout<<"Rows in below table show the number of overs left"<<endl;
    cout<<"Columns in below table show the number of wickets in hand"<<endl;
    cout<<" \t";
    for(int j=1;j<number_of_wickets;j++)
    {
        cout<<j<<"\t";
    }
    cout<<endl;
    for(int i=6;i<number_of_balls;i+=6)
    {
        cout<<i/6<<"\t";
        for(int j=1;j<number_of_wickets;j++)
        {
            cout<<dp[i][j]<<"\t";
        }
        cout<<endl;
    }
}