# Suffix Arrays: Knuth-Morris-Pratt Algorithm for Exact Pattern Matching

__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/specializations/data-structures-algorithms. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)
<br/>
<br/>
__Assignment Description:__
<br/>
Problem Introduction:
In this problem, we ask a simple question: how many times one string occurs as a substring of another?
Recall that different occurrences of a substring can overlap with each other. For example, ATA occurs three
times in CGATATATCCATAG.
<br/>
<br/>
Task: Find all occurrences of a pattern in a string.
<br/>
<br/>
Input Format: Strings 𝑃𝑎𝑡𝑡𝑒𝑟𝑛 and 𝐺𝑒𝑛𝑜𝑚𝑒.
<br/>
<br/>
Constraints: 1 ≤ |𝑃𝑎𝑡𝑡𝑒𝑟𝑛| ≤ 106; 1 ≤ |𝐺𝑒𝑛𝑜𝑚𝑒| ≤ 106; both strings are over A, C, G, T.
<br/>
<br/>
Output Format: All starting positions in 𝐺𝑒𝑛𝑜𝑚𝑒 where 𝑃𝑎𝑡𝑡𝑒𝑟𝑛 appears as a substring (using 0-based
indexing as usual).
<br/>
<br/>
Time Limits: Python - 10 seconds
<br/>
<br/>
Memory Limit. 512MB.
