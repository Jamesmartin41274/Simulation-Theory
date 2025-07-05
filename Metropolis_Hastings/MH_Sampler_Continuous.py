import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#The aim here is to implement a basic MH MC algorithm to compute a fake posterior distribution to estimate the parameter theta.
#The state space here is continuous since the support of the parameters posterior distribution lies over the Real axis. 

# Defined parameters are:
x0 = 0.0
mu, tau = 0.0, 2.0
sigma = 4
N = 10000

# Functions
def f(x,mu,tau):
    """This is a function for the target distribution"""
    posterior_distribution = norm.pdf(x, loc = mu, scale = tau )
    return(posterior_distribution)

def g(x_t,sigma):
    """Proposal distirbution for Y = x+z where z~N(0,sigma^2)
       Sigma represents the standard deviation of the random variable Z.
       x_t is current position of the Random Vriable.
       Outputs y a pertubated value which is the proposal move value. 
    """
    z = np.random.normal(loc=0,scale=sigma)
    y = x_t + z 
    return(y)


def alpha_ratio(fy,fx):
    """The first thing to note here is that in the Metropolis-Hastings algorithm q(y|x)=q(x|y).
    Thus, the ratio is significantly simplified yielding a slightly simpler ratio.
    Computes the ratio and outputs the alpha value. 
    """
    alpha = np.minimum(1,fy/fx)
    return(alpha)


def MH_propose_and_accept(x,mu,tau,sigma):
    """"Computes the alpha ratio for the accept/reject proposal then computes the proposal"""
    y = g(x,sigma)
    fx = f(x,mu,tau)
    fy= f(y,mu,tau)
    alpha_value = alpha_ratio(fy,fx)
    u = np.random.uniform(0,1)
    if u<=alpha_value:
        return(y)
    else:
        return(x)
    
def run_MH(x_0,mu,tau,sigma,N):
    """Run N iterations of the MH sampler starting at x_0; returns array of samples."""
    x=x_0
    samples = []
    for i in range(N):
        x = MH_propose_and_accept(x, mu, tau, sigma)
        samples.append(x)
    return(np.array(samples))


# Running the system with required inputs
samples = run_MH(x0,mu,tau,sigma,N)

# Acceptance rate
moves = samples[1:] != samples[:-1] # Boolean Array of length N
accept_n = np.sum(moves)
acceptance_rate =accept_n/N
print("Acceptance rate:", acceptance_rate)

# Burn in on the sample
burn_in = int(0.1*len(samples)) #Allows a burn in for MH algorithm I set it as the first 10%
post_burn_in = samples[burn_in:] #Samples with burn in removed

# Plotting the histrogram of the samples distribution
plt.hist(post_burn_in, bins = 50,density = True,alpha = 0.5,label="Accepted samples")

# Plotting the target function
x_vals = np.linspace(-10,10,10000)
pdf_vals = norm.pdf(x_vals, loc = mu,scale = tau)
plt.plot(x_vals,pdf_vals, color = 'r',lw=2,label="Target pdf")

plt.legend()
plt.grid(True)
plt.xlabel("x values")
plt.ylabel("pdf values")
plt.title("MCMC Metroplois Hastings algorithm for a Gaussian distribution target function")
plt.show()

# Proposal jumps and acceptance rate
plt.plot(samples)
plt.xlabel("Iteration")
plt.ylabel("θ value")
plt.title("Trace of the MH chain")
plt.show()