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
    // need 4 dps
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    double dp[number_of_balls][number_of_wickets];
    string play_style[number_of_balls][number_of_wickets];
    fo(i,number_of_balls)
    {
        dp[i][0]=0;
        play_style[i][0]='-';
    }
    fo(i,number_of_wickets)
    {
        dp[0][i]=0;
        play_style[0][i]='-';
    }
    for(int i=1;i<number_of_balls;i++)
    {
        for(int j=1;j<number_of_wickets;j++)
        {
            double dp_g,dp_m,dp_b;
            double dp_gd,dp_gs,dp_ga,dp_md,dp_ms,dp_ma,dp_bd,dp_bs,dp_ba;
            dp_gd = (0.02*dp[i-1][j-1])+(0.98*dp[i-1][j]) +0.03;
            dp_gs = (0.1*dp[i-1][j-1])+(0.9*dp[i-1][j]) +0.5;
            dp_ga = (0.2*dp[i-1][j-1])+(0.8*dp[i-1][j]) +1;
            dp_g=max({dp_gd,dp_gs,dp_ga});
            dp_md = (0.01*dp[i-1][j-1])+(0.99*dp[i-1][j]) +0.05;
            dp_ms = (0.05*dp[i-1][j-1])+(0.95*dp[i-1][j]) +0.65;
            dp_ma = (0.15*dp[i-1][j-1])+(0.85*dp[i-1][j]) +1.5;
            dp_m=max({dp_md,dp_ms,dp_ma});
            dp_bd = (0.001*dp[i-1][j-1])+(0.999*dp[i-1][j]) +0.07;
            dp_bs = (0.01*dp[i-1][j-1])+(0.99*dp[i-1][j]) +0.8;
            dp_ba = (0.02*dp[i-1][j-1])+(0.98*dp[i-1][j]) +2;
            dp_b=max({dp_bd,dp_bs,dp_ba});

            if(dp_g==dp_gd)
            {
                play_style[i][j].push_back('d');
            }
            else if(dp_g==dp_gs)
            {
                play_style[i][j].push_back('s');
            }
            else if(dp_g==dp_ga)
            {
                play_style[i][j].push_back('a');
            }
            if(dp_m==dp_md)
            {
                play_style[i][j].push_back('d');
            }
            else if(dp_m==dp_ms)
            {
                play_style[i][j].push_back('s');
            }
            else if(dp_m == dp_ma)
            {
                play_style[i][j].push_back('a');
            }
            if(dp_b==dp_bd)
            {
                play_style[i][j].push_back('d');
            }
            else if(dp_b==dp_bs)
            {
                play_style[i][j].push_back('s');
            }
            else
            {
                play_style[i][j].push_back('a');
            }

            dp[i][j]=(dp_b+dp_g+dp_m)/3;
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
            // cout<<dp[i][j]<<"\t";
            cout<<play_style[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<"a stands for attack\t s stands for strike rotation\t d stands for defence"<<endl;
}