#Input: N,K,W where:

#N: prob when u have N or less points
#K: Alice stop once hitting K
#W: range [1....w] of points you can get

#Alice starts with 0, stops playing when she has K or more points, and draw [1...w] at a time
#the answer is the probability that when she stops, she obtains N or less points

#Step 1. Analyze stop conditions and different N for intuition
#When alice stops, she can get K,K+1,..K+W-1 points

#Design: our idea is, create a dp array of length N+W+1
#where dp[i] denote the answer when we are at a stage of having i points,  working backwards
#when she has k,k+1,...k+n-1 points she stops drawing 
