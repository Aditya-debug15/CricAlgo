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
#define vpi vector<pair<int,int>>
#define prob_wicket 0.05
#define prob_dot 0.3
#define prob_1 0.4
#define prob_2 0.07
#define prob_3 0.004
#define prob_4 0.114
#define prob_5 0.00016
#define prob_6 0.055
#define number_of_balls 121 // 0 - 120 need both for dp state so that is why 121
#define number_of_wickets 11 // 0 -10
#define score_max 250
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    double dp[number_of_balls][score_max+1][number_of_wickets];

    // BASE STATE - 1
    for(int s=0;s<=score_max;s++)
    {
        for(int i=0;i<number_of_wickets;i++)
        {
            dp[0][s][i]=0;
        }
    }

    // BASE STATE - 2
    for(int n=0;n<number_of_balls;n++)
    {
        for(int s=0;s<=score_max;s++)
        {
            dp[n][s][0]=0;
        }
    }

    // base state - 3
    for(int n=0;n<number_of_balls;n++)
    {
        for(int i=0;i<number_of_wickets;i++)
        {
            dp[n][0][i]=1;
        }
    }

    // transition
    for(int n=1;n<number_of_balls;n++)
    {
        for(int s=1;s<=score_max;s++)
        {
            for(int i=1;i<number_of_wickets;i++)
            {
                if(s==1)
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1 + prob_2 + prob_3 + prob_4 +prob_5 +prob_6); 
                else if(s==2)
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1*dp[n-1][s-1][i]) + (prob_2 + prob_3 + prob_4 +prob_5 +prob_6); 
                else if(s==3)
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1*dp[n-1][s-1][i]) + (prob_2*dp[n-1][s-2][i])+ (prob_3 + prob_4 +prob_5 +prob_6); 
                else if(s==4)
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1*dp[n-1][s-1][i]) + (prob_2*dp[n-1][s-2][i]) + (prob_3*dp[n-1][s-3][i]) + (prob_4 +prob_5 +prob_6); 
                else if(s==5)
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1*dp[n-1][s-1][i]) + (prob_2*dp[n-1][s-2][i]) + (prob_3*dp[n-1][s-3][i]) + (prob_4*dp[n-1][s-4][i]) +(prob_5 +prob_6); 
                else if(s==6)
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1*dp[n-1][s-1][i]) + (prob_2*dp[n-1][s-2][i]) + (prob_3*dp[n-1][s-3][i]) + (prob_4*dp[n-1][s-4][i]) +(prob_5*dp[n-1][s-5][i]) +(prob_6); 
                else
                    dp[n][s][i] = (prob_wicket*dp[n-1][s][i-1]) + (prob_dot*dp[n-1][s][i]) + (prob_1*dp[n-1][s-1][i]) + (prob_2*dp[n-1][s-2][i]) + (prob_3*dp[n-1][s-3][i]) + (prob_4*dp[n-1][s-4][i]) +(prob_5*dp[n-1][s-5][i]) +(prob_6*dp[n-1][s-6][i]); 
            }
        }
    }
    // So dp is ready

    cout<<"The probability of winning when 10 wickets are in hand and 20 overs left"<<endl;
    for(int s=70;s<=250;s+=10)
    {
        cout<<"score :"<<s<<" win chance :"<<dp[120][s][10]<<endl;
    }
    cout<<"Keeping score fixed to be 120 and over 15 and varing wickets"<<endl;
    for(int i=0;i<number_of_wickets;i++)
    {
        cout<<"Wicket in hand:"<<i<<" win chance :"<<dp[90][120][i]<<endl;
    }
}