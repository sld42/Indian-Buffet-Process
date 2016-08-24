# Indian-Buffet-Process
Python code that demonstrates how data generated from an IBP changes as you vary the process hyperparameters

The purpose of this code is to demonstrate how each of the parameters of the IBP change the way data is generated. It is not to perform inference. 

The Indian Buffet Process (IBP) is a Bayesian nonparametric method for unsupervised learning. The IBP can determine the number of latent variables that generated the observed data without having the user to initially specify the number of latent variables. 

The IBP generates binary matrices by having "customers" arrive at a buffet line and select dishes. The intial customer selects a certain number of dishes based on a draw from a Poisson distribution. The following customers select old dishes with probability determined by the number of times a customer has visited that dish in a "rich get richer" fashion. The customer then selects a number of new dishes based on a Poisson distribution. 

The IBP is parameterized by alpha, a parameter of the Poisson distribution, and N, the number of customers in the restaurant. Larger values of alpha result in more dishes visited for a fixed number of customers. Large values of N also increase the number of dishes visited by customers, but there reaches a point of diminishing returns for fixed alpha.

A more in-depth examination of these plots is provided in the "IBP.pdf" file. 

![](images/figure_1.png?raw=true)

![](images/figure_4.png?raw=true)
