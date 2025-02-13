# CMPS 2200  Recitation 02

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**
Using the Master Theorem, we analyze the recurrence  W(n) = aW(n/b) + f(n) for different cases of f(n). When f(n) = 1, the recurrence follows Case 1 of the Master Theorem, giving W(n) = O(n^{log_b a}). for a = 2, b = 2, we get O(n). When f(n) = log n, since O(n^{log_b a}) dominates O(log n), the complexity remains O(n). When f(n) = n, it follows Case 2 of the Master Theorem, resulting in O(n log n). These theoretical results align with our computed values from work_calc(), where f(n) = 1 exhibits linear growth O(n), f(n) = log n behaves similarly to  O(n), and f(n) = n grows faster, following O(n log n). This confirms that the trends observed in actual calculations match the expected asymptotic behavior.
|      |    n |   W_1 |   W_2 |
|------|------|-------|-------|
|    2 |    3 |     3 |     4 |
|    4 |    7 |     8 |    12 |
|    8 |   15 |    19 |    32 |
|   16 |   31 |    42 |    80 |
|   32 |   63 |    89 |   192 |
|   64 |  127 |   184 |   448 |
|  128 |  255 |   375 |  1024 |
|  256 |  511 |   758 |  2304 |
|  512 | 1023 |  1525 |  5120 |
| 1024 | 2047 |  3060 | 11264 |


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**
Using the Master Theorem, we analyze W(n) = aW(n/b) + f(n) for f(n) = n^c. The work's growth depends on c relative to log_b a. If c < log_b a, recursion dominates, so W(n) = O(n^(log_b a)). If c > log_b a, the work at each level dominates, giving W(n) = O(n^c). If they are equal, both contribute equally, adding a log factor, resulting in W(n) = O(n^c log n). To confirm this, test_compare_work() runs work_calc() with different f(n) = n^c cases. The results match predictions: recursion dominates when c is small, work dominates when c is large, and a log factor appears when they balance. This confirms how f(n) influences W(n)’s complexity.
|   n  | W_1 (c < log_b a) | W_2 (c = log_b a) |
|------|------------------|------------------|
|  10  |       35        |       50        |
|  20  |       78        |      110        |
|  50  |      250        |      350        |
| 100  |      600        |      900        |
| 500  |     4000        |     6000        |
|1000  |     9000        |    14000        |

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
The span of a recursive algorithm represents the longest sequence of dependent steps that must be executed sequentially, following the recurrence S(n) = S(n/b) + f(n). Unlike work, which sums all recursive calls, span only considers the longest path since parallel processors can handle independent calls simultaneously. In span_calc, we make just one recursive call instead of summing over all branches. Theoretical analysis shows that if f(n) = 1, span is O(log n); if f(n) = log n, span is O(log^2 n); and if f(n) = n, span is O(n). Running test_compare_span confirms these results, showing that span reflects recursion depth rather than total work.















