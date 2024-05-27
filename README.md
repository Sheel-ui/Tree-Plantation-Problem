# Tree-Plantation-Problem

## Problem Definition 
The project focuses on developing an algorithm to optimize tree planting in the town of Greenvale, where each plot of land has a minimum tree requirement assigned by the Parks and Recreation Department. The goal is to find the largest possible square-shaped area of plots within the town that meets specific tree planting criteria.
<p></p>
<b> Problem 1: Maximum Square Area for Minimum Tree Requirement </b>
<p>Given a matrix p of dimensions m × n, representing the minimum number of trees required on each plot, and an integer h (positive), the algorithm aims to find the bounding indices of a square area where each plot enclosed requires a minimum of h trees to be planted.</p>

<b> Problem 2: Maximum Square Area with Corner Plot Flexibility </b>
<p>Similar to Problem 1, but with the additional flexibility that corner plots can have any number of trees required. The goal is to find the bounding indices of a square area where all but the corner plots enclosed require a minimum of h trees to be planted.</p>

<b> Problem 3: Limited Exception for Minimum Tree Requirement </b>
<p>Given the matrix p, an integer h (positive), and an additional parameter k (positive) representing the maximum number of plots that can have a minimum tree requirement of less than h, the algorithm aims to find the bounding indices of a square area meeting these criteria.</p>


## Steps to run
To execute algorithm use python3 main.py ALG#, where # is algorithm no.

For example, to execute alg3
```
$ python3 main.py alg3
```
## Algorithms Included

<b> For Problem 1 </b>

| Algorithm | Time Complexity | Space Complexity |
| ------- | ------- | ------- |
| alg1 (Brute Force)   | O(m<sup>3</sup>n<sup>3</sup>)   | O(1)   |
| alg2   | O(m<sup>2</sup>n<sup>2</sup>)   | O(1)   |
| alg3 (Dynamic Programming)   | O(mn)   | O(mn)   |

<b> For Problem 2 </b>
| Algorithm | Time Complexity | Space Complexity |
| ------- | ------- | ------- |
| alg4 (Dynamic Programming)   | O(mn<sup>2</sup>   | O(mn<sup>2</sup>)   |
| alg5a (Top Down Recursion + Memoization)   | O(mn)  | O(mn)  |
| alg5b (Bottom Up DP)   | O(mn)   | O(mn)   |

<b> For Problem 3 </b>
| Algorithm | Time Complexity | Space Complexity |
| ------- | ------- | ------- |
| alg6 (Brute Force)   | O(m<sup>3</sup>n<sup>3</sup>)   | O(1) |
| alg7a (Top Down Recursion + Memoization)   | O(mnk)   | O(1)   |
| alg7b (Bottom Up DP)   | O(mnk)   | O(1)   |

## Experimental Comparative Study

Following figures depict visual representations illustrating the execution time needed for various tasks across different input sizes, with m=n, h, and randomly generated matrix values.

 ### *Problem1:*

 <p align="center">
  <img src="./Experimental%20Comparision/Problem1_allTasks.PNG" width="500px">
</p>
 <p align="center">
  <img src="./Experimental%20Comparision/Problem1_Task2&3.PNG" width="500px">
</p>

 
  ### *Problem2:*

<p align="center">
  <img src="./Experimental%20Comparision/Problem2.PNG" width="500px">
</p>
 <p align="center">
  <img src="./Experimental%20Comparision/Problem2_task5a&5b.PNG" width="500px">
</p>


  ### *Problem3:* 
  <p align="center">
  <img src="./Experimental%20Comparision/Problem3.PNG" width="500px">
</p>


## Implementation Details
For detailed implementation information, please refer to the [project report](ProjectReport.pdf).
