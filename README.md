### Sine Cosine Algorithm

##### Reference: Mirjalili S. SCA: A Sine Cosine Algorithm for solving optimization problems[J]. Knowledge-Based Systems, 2016, 96.

| Variables  | Meaning                                               |
| ---------- | ----------------------------------------------------- |
| pop        | The number of candidates                              |
| iter       | The number of iterations                              |
| lb         | The lower bound (list)                                |
| ub         | The upper bound (list)                                |
| pos        | The position of all candidates (list)                 |
| score      | The score of all candidates (list)                    |
| dim        | Dimension                                             |
| gbest      | The position of the global best candidate             |
| gbest_pos  | The score of the global best candidate (list)         |
| seed_pos   | The position of the seeds of the ith candidate (list) |
| seed_score | The score of the seeds of the ith candidate (list)    |
| iter_best  | The global best score of each iteration (list)        |
| con_iter   | The last iteration number when "gbest" is updated     |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Sine-Cosine-Algorithm/blob/main/Pressure%20vessel%20design.png)

$$
\begin{align}
&\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
&\text{s.t.} \\
&-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
\end{align}
$$

#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    pop = 30
    iter = 1000
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Sine-Cosine-Algorithm/blob/main/convergence%20curve.png)

The SCA converges at its 957-th iteration, and the global best value is 9590.464425690781. 

```python
{
    'best score': 9590.464425690781, 
    'best solution': [1.457576369166947, 0.6612071818606331, 68.48174413611495, 17.286314289498986], 
    'convergence iteration': 957
}
```

