# RHS_Robustness
### A toy example: A facility location allocation problem

To supply a commodity to customers, it will be first stored at  $`\textcolor{blue}{m}`$ 
potential facilities and then be transported to $`\textcolor{blue}{n}`$ customers. 
The fixed cost of the building facilities at site $`\textcolor{blue}{i}`$ is 
$`\textcolor{blue}{f_i}`$ and the unit capacity cost is $`\textcolor{blue}{a_i}`$
for $`\textcolor{blue}{i = 1,\ldots,m}`$. The demand is $`\textcolor{blue}{d_j}`$ for
$`\textcolor{blue}{j = 1, \ldots, n}`$, and the unit transportation cost between
$`\textcolor{blue}{i}`$ and $`\textcolor{blue}{j}`$ is $`\textcolor{blue}{c_{ij}}`$. 
Let $`\textcolor{blue}{y_i \in \{0, 1\}}`$ be the 
facility location variable, and $`\textcolor{blue}{x_{ij} \in \mathbb{R}_+}`$ be the 
transportation variable.

Suppose that the demand parameter is not deterministic and following a Normal 
Distribution, e.g. \textcolor{blue}{$N(\mu=200,\sigma=50)$}.
We build the following Chance-constrained Mathematical Programming,




```math
\begin{equation}
\nonumber
\begin{split}
\textbf{min} \quad &\sum_i f_iy_i + \sum_i \sum_j c_{ij} x_{ij} \\
\text{s.t.} \quad &\sum_j  x_{ij} \leq My_i, \quad \forall i, \\
&\sum_i  x_{ij} \geq \tilde{d}_j , \quad \forall j, \\
&y_i \in \{0, 1\}, \quad x_{ij} \geq 0,\quad \forall i,j. 
\end{split}
\end{equation}
```
