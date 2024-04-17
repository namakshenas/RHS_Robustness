# RHS Robustness
### A toy example: A facility location-allocation problem

To supply a commodity to customers, it will be first stored at  $`\textcolor{blue}{m}`$ 
potential facilities and then be transported to $`\textcolor{blue}{n}`$ customers. 
The fixed cost of the building facilities at site $`\textcolor{blue}{i}`$ is 
$`\textcolor{blue}{f_i}`$. The demand is $`\textcolor{blue}{d_j}`$ for
$`\textcolor{blue}{j = 1, \ldots, n}`$, and the unit transportation cost between
$`\textcolor{blue}{i}`$ and $`\textcolor{blue}{j}`$ is $`\textcolor{blue}{c_{ij}}`$. 
Let $`\textcolor{blue}{y_i \in \{0, 1\}}`$ be the 
facility location variable, and $`\textcolor{blue}{x_{ij} \in \mathbb{R}_+}`$ be the 
transportation variable.

Suppose that demand parameter $`\textcolor{red}{\tilde{d}_j}`$ are not deterministic and their 
respective stochastic 
states are oscillating within known threshold
$`\textcolor{red}{\tilde{d}_j \in [d_j-\hat{d}_j,d_j+\hat{d}_j]}`$.


```math
\begin{equation}
\nonumber
\begin{split}
\textbf{min} \quad &\sum_i f_iy_i + \sum_i \sum_j c_{ij} x_{ij} \\
\text{s.t.} \quad &\sum_j  x_{ij} \leq My_i, \quad \forall i, \\
&\sum_i  x_{ij} \geq \textcolor{red}{\tilde{d}_j} , \quad \forall j, \\
&y_i \in \{0, 1\}, \quad x_{ij} \geq 0,\quad \forall i,j. 
\end{split}
\end{equation}
```

The robust counterpart based on my new concept is as follows.

```math
\begin{equation}
\nonumber
\begin{split}
\textbf{min} \quad &\sum_i f_iy_i + \sum_i \sum_j c_{ij} x_{ij} \\
\text{s.t.} \quad &\sum_j  x_{ij} \leq My_i, \quad \forall i, \\
&\sum_i  x_{ij} \geq d_j , \quad \forall j, \\
&\sum_i  (z_i^l + z_i^u) \leq \frac{\Gamma \sum_j d_j}{m^2} , \\
&d_i - \hat{d}_j - \sum_i  c_{ij} x_{ij} \leq z_i^l , \quad \forall j,\\
&d_i + \hat{d}_j - \sum_i  c_{ij} x_{ij} \leq z_i^u , \quad \forall j,\\
&y_i \in \{0, 1\}, \quad x_{ij},z_i^l,z_i^u \geq 0,\quad \forall i,j. 
\end{split}
\end{equation}
```

where $`\frac{\Gamma \sum_i d_i}{m^2}`$ is translated as
`mean absolute deviation from the mean (MAD)`. **Note that $`\Gamma`$ can take any real number**.

> Proof. The detail of the proof is not provided here. However, as a hint, I forced `Edmundson-Mandasky bound (1956)`
and `Bental-Hochman bound (1972)` on the condensed left-hand side.



### Figure: Price of Robustness!
I ran a quick experiment based on the following numerical inputs and different gamma values:

```
f = [120, 150, 135]
d = [50, 20, 40, 70, 10]
c = [[10, 20, 15, 16, 17],
     [5, 17, 18, 15, 15],
     [13, 15, 18, 15, 16]]
d_hat = 0.2 d
```
![](https://github.com/namakshenas/RHS_Robustness/blob/main/fig.png)

### Refs
> Ben-Tal, A., & Hochman, E. (1972). More bounds on the expectation of a convex function of a
random variable. 
Journal of Applied Probability, 9(4), 803-812.

> Madansky, A. (1959). Bounds on the expectation of a convex function of 
a multivariate random variable. 
The Annals of Mathematical Statistics, 30(3), 743-746.
