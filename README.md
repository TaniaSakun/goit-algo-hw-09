# goit-algo-hw-09
The repository for the 9th GoItNeo Basic Algorithms homework: Greedy algorithms and dynamic programming

### To run the project please complete the following steps:

pip install -r requirements.txt or pip3 install -r requirements.txt

python main.py or python3 main.py

## Results of execution
Execution time **before** caching results for **100** iterations :

        Greedy         : 0.06 ms
        Min            : 0.07 ms
        Min with LRU   : 0.06 ms

Execution time **after** caching results for **100** iterations :

        Greedy         : 0.05 ms
        Min            : 0.04 ms
        Min with LRU   : 0.04 ms

Execution time **before** caching results for **1000** iterations :

        Greedy         : 0.05 ms
        Min            : 0.03 ms
        Min with LRU   : 0.04 ms

Execution time **after** caching results for **1000** iterations :

        Greedy         : 0.48 ms
        Min            : 0.23 ms
        Min with LRU   : 0.38 ms

Execution time **before** caching results for **10000** iterations :

        Greedy         : 0.05 ms
        Min            : 0.02 ms
        Min with LRU   : 0.04 ms

Execution time **after** caching results for **10000** iterations :

        Greedy         : 4.70 ms
        Min            : 1.89 ms
        Min with LRU   : 3.57 ms

Based on the provided execution times before and after caching results for different numbers of iterations, we can draw the following conclusions:

## Greedy Algorithm:

Execution time increases significantly as the number of iterations increases, both before and after caching results.
It has the lowest execution time before caching results but becomes significantly slower compared to dynamic programming after caching results, especially for a large number of iterations.
The execution time increases linearly with the number of iterations.

## Dynamic Programming (Min):

Execution time decreases with caching results, indicating that caching improves performance.
It has relatively lower execution time compared to the greedy algorithm, especially after caching results.
The execution time remains stable or decreases slightly as the number of iterations increases.

## Dynamic Programming with LRU Cache (Min with LRU):

Similar to dynamic programming, execution time decreases with caching results.
It has slightly higher execution time compared to dynamic programming without caching, likely due to the overhead of caching.
The execution time remains relatively stable as the number of iterations increases, similar to dynamic programming.

## Conclusion:

For a small number of iterations, the greedy algorithm may perform slightly better than dynamic programming.
However, as the number of iterations increases, dynamic programming, especially with caching, outperforms the greedy algorithm significantly.
Dynamic programming with LRU caching provides improved performance compared to the greedy algorithm, although it may have slightly higher overhead due to caching.
Overall, dynamic programming, particularly with caching, is more efficient for this coin exchange problem, especially for a large number of iterations.
