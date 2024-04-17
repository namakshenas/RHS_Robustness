# RHS_Robustness
Right-Hand-Side Robustness
To supply a commodity to customers, it will be first stored at $$\textcolor{blue}{$m$}$$ 
potential facilities and then be transported to \textcolor{blue}{$n$} customers. 
The fixed cost of the building facilities at site \textcolor{blue}{$i$} is 
\textcolor{blue}{$f_i$} and the unit capacity cost is \textcolor{blue}{$a_i$}
for \textcolor{blue}{$i = 1,\ldots,m$}. The demand is \textcolor{blue}{$d_j$} for
\textcolor{blue}{$j = 1, \ldots, n$}, and the unit transportation cost between
\textcolor{blue}{$i$} and \textcolor{blue}{$j$} is \textcolor{blue}{$c_{ij}$}.
The maximal allowable capacity of the facility at site \textcolor{blue}{$i$} 
is \textcolor{blue}{$K_i$}. Let \textcolor{blue}{$y_i \in \{0, 1\}$} be the 
facility location variable, \textcolor{blue}{$z_i \in \mathbb{R}_+$} be the
capacity variable, and \textcolor{blue}{$x_{ij} \in \mathbb{R}_+$} be the 
transportation variable.

Suppose that the demand parameter is not deterministic and following a Normal 
Distribution, e.g. \textcolor{blue}{$N(\mu=200,\sigma=50)$}.
We build the following Chance-constrained Mathematical Programming,


$$
\begin{equation}
\nonumber
\begin{split}
\textbf{minimize} \quad &\sum_i f_iy_i + \sum_i a_iz_i + \sum_i \sum_j c_{ij} x_{ij} \\
\text{subject to} \quad &z_i \leq K_iy_i, \; \forall i,\\
&\sum_j  x_{ij} \leq z_i, \; \forall i, \\
&\Pr \left\{\sum_i  x_{ij} \geq \tilde{d}_j \right\} \geq 1-\alpha, \; \forall j, \\
&y_i \in \{0, 1\}, z_i \geq 0, \; \forall i, \quad x_{ij} \geq 0,\; \forall i,j. 
\end{split}
\end{equation}
$$