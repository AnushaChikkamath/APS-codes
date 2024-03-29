# -*- coding: utf-8 -*-
"""Jobs_scheduling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E2kHuZR2DEHfakqJm8BO3TGSoRI-8lGV
"""

"""
  Job sequencing problem:

  You are given a set of N jobs where each job comes with a deadline and profit.
  The profit can only be earned upon completing the job within its deadline. 
  Find the number of jobs done and the maximum profit that can be obtained. 
  Each job takes a single unit of time and only one job can be performed at a time.

  Input- N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
  Output- 2 60

"""

class Job:
  def __init__(self,id,deadline,profit):
    self.id=id
    self.deadline=deadline
    self.profit=profit

class Solution:

  def jobs_sequencing(self,jobs):

    jobs.sort(key=lambda x: x.profit, reverse=True)
    maxi=jobs[0].deadline
    for i in range(1,len(jobs)):
      maxi=max(maxi,jobs[i].deadline)

    slot = [-1] * (maxi + 1)
    countJobs = 0
    jobProfit = 0

    for i in range(0,len(jobs)):
      for j in range(jobs[i].deadline,0,-1):
        if(slot[j]==-1):
          slot[j]=i
          countJobs=countJobs+1
          jobProfit=jobProfit+jobs[i].profit
          break

    return countJobs,jobProfit



if __name__=="__main__":
  n=int(input('Enter the number of jobs'))
  print('Enter the id, deadline and profit of each job')
  jobs=[]
  for i in range(n):
    a,b,c=(map(int,input().split()))
    jobs.append(Job(a,b,c))
  count,profit=Solution().jobs_sequencing(jobs)
  print(f'The maximum count of jobs that can be performed is {count}.')
  print(f'The maximum profit that can be obtained is {profit}.')

1