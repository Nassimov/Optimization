# Generate data for SVM classifier with L1 regularization.
from __future__ import division
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

def implement_SVR ( norm ,constraint = False ) :

    #generating a random dataset

    #this seed allows us to generate the same dataset everytime we run the code with seed(1)
    np.random.seed(1)

    nr_features = 20
    training_nr = 1000
    test_nr = 1000
    DENSITY = 0.2
    beta_true = np.random.randn(nr_features,1)
    indexs = np.random.choice(nr_features, int((1-DENSITY)*nr_features), replace=False)
    for index in indexs:
        beta_true[index] = 0
    sigma = 45
    X = np.random.normal(0, 5, size=(training_nr,nr_features))
    Y = np.sign(X.dot(beta_true) + np.random.normal(0,sigma,size=(training_nr,1)))
    X_test = np.random.normal(0, 5, size=(test_nr,nr_features))

    # Form SVM regularization problem.

    beta = cp.Variable((nr_features,1))
    v = cp.Variable()
    loss = cp.sum(cp.pos(1 - cp.multiply(Y, X @ beta - v)))
    lambd = cp.Parameter(nonneg=True)

    if ( (constraint == True) and (norm == 1) ) :
        beta_plus = cp.Variable()
        beta_minus = cp.Variable()
        reg = beta_plus + beta_minus
        # Create constraints 
        constraints = [
            beta_plus - beta_minus == beta,
            beta_plus >= 0,  beta_minus >= 0
            ]
        prob = cp.Problem(cp.Minimize(loss/training_nr + lambd*reg), constraints)
    
    elif ( (constraint == True) and (norm == 'inf') ) :
        beta_max = cp.Variable() 
        constraints = [
            np.sum(beta) <= beta_max
            ]
        reg = cp.norm(beta, 'inf') 
        prob = cp.Problem(cp.Minimize(loss/training_nr + lambd*reg), constraints)

    elif (constraint == False):
        #no constraints in this case, use the norm
        reg = cp.norm(beta, norm) 
        prob = cp.Problem(cp.Minimize(loss/training_nr + lambd*reg))

    # Compute a trade-off curve and record train and test error.
    trials = 100
    train_error = np.zeros(trials)
    test_error = np.zeros(trials)
    lambda_vals = np.logspace(-2, 0, trials)
    beta_vals = []
    for i in range(trials):
        lambd.value = lambda_vals[i]
        prob.solve()
        train_error[i] = (np.sign(X.dot(beta_true) ) != np.sign(X.dot(beta.value) - v.value)).sum()/training_nr
        test_error[i] = (np.sign(X_test.dot(beta_true) ) != np.sign(X_test.dot(beta.value) - v.value)).sum()/test_nr
        beta_vals.append(beta.value)
        
    # Plot the train and test error over the trade-off curve.
    plt.plot(lambda_vals, train_error, label="Train error")
    plt.plot(lambda_vals, test_error, label="Test error")
    plt.xscale('log')
    plt.legend(loc='upper left')
    plt.xlabel(r"$\lambda$", fontsize=16)
    plt.show()

implement_SVR ( "inf", constraint=True ) 