# Longest Processing Time and Optimized Longest Processing Time Algorithm

### Problem Statement
Given a set of J jobs where j[i] has a length of l (execution time) and a
number of available processors m. What is the minimum possible time required
to schedule all jobs in J on m processors such that:
1. No Jobs Overlap
2. Loads on the processors are optimized

### Solution
Implement a regular Longest Processing Time. Bound the number of processors
based on the ideal load calculated using the Optimized Longest Processing Time
Algorithm.

## How is the ideal number of processors calculated?
Load balance the tasks such that all processors have almost equal load. The
total number of processors required for such a load balancing will be the 
optimal processors.

Choose the lower of available processors, optimal processors as the ideal
number of processors.

## Longest Processing Time

### Description:
A simple, often-used multiprocessor scheduling (load balancing) algorithm
is the LPT algorithm (Longest Processing Time) which sorts the jobs by its
processing time and then assigns them to the machine with the earliest
end time so far. This algorithm achieves an upper bound of 4/3 - 1/(3m) OPT.

### Problem Statement:
"Given a set J of jobs where job ji has length li and a number of processors m,
what is the minimum possible time required to schedule all jobs in J on
m processors such that none overlap?"

### Background:
In computer science, multiprocessor scheduling is an NP-hard optimization
problem. The applications of this problem are numerous, but are, as suggested
by the name of the problem, most strongly associated with the scheduling of
computational tasks in a multiprocessor environment.

## Optimized Longest Processing Time

### Description:
An Optimized LPT algorithm schedules jobs on processors such that loads on
the processors are almost equal and uses minimum number of processors.

### Advantages:
1. Better resource usage
2. Almost equal run times on processors

### Bottleneck and Dependency:
1. The upper bound of processors is dependent on largest task by time

