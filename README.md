# Metropolis–Hastings MCMC Sampler for a Gaussian Posterior

A minimal Python implementation of the Random-Walk Metropolis algorithm to draw samples from a univariate Normal\((\mu,\tau^2)\) “posterior” (here treated as a target distribution). By default the target is \(N(0,2^2)\), but you can change `mu` and `tau` at the top of the script.

---

## Project Structure

- `MH_Sample_Continuous.py` — main script containing all functions and the sampling driver.
- `requirements.txt` — lists dependencies (`numpy`, `matplotlib`, `scipy`).

---

## Description

This project implements a simple Metropolis–Hastings MCMC sampler in Python. It consists of five core functions:

1. **`f(x, mu, tau)`**  
   Returns the target density value:
   \[
     p(x) \propto \exp\!\bigl(-\tfrac{(x-\mu)^2}{2\tau^2}\bigr)
   \]
   at point `x`.

2. **`g(x_t, sigma)`**  
   Proposes a new candidate `y` via a Gaussian random-walk:
   \[
     y = x_t + Z,\quad Z \sim N(0,\sigma^2).
   \]
   Here `sigma` is the proposal standard deviation (default = 4).

3. **`alpha_ratio(fy, fx)`**  
   Computes the Metropolis acceptance ratio
   \[
     \alpha = \min\{1,\,fy/fx\}
   \]
   (uses the symmetry \(q(y\mid x)=q(x\mid y)\)).

4. **`MH_propose_and_accept(x, mu, tau, sigma)`**  
   Executes one MH update:
   1. Calls `g` to get a candidate `y`.  
   2. Evaluates `fx = f(x, mu, tau)` and `fy = f(y, mu, tau)`.  
   3. Computes `alpha = alpha_ratio(fy, fx)`.  
   4. Draws `u ~ Uniform(0,1)`.  
   5. Returns `y` if `u <= alpha`, otherwise returns `x`.

5. **`run_MH(x0, mu, tau, sigma, N)`**  
   Runs the MH sampler for `N` iterations starting from `x0` and returns a NumPy array of samples.

The top of the script sets the parameters:
```python
x0    = 0.0      # initial state
mu    = 0.0      # target mean
tau   = 2.0      # target std. dev.
sigma = 4.0      # proposal std. dev.
N     = 10000    # number of iterations
