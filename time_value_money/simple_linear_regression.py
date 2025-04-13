import numpy as np

def total(data):
    """Simple Sum, given array-like object: data"""
    sum_data = 0
    for x in data:
        sum_data += x
    return sum_data

def mean(data):
    """Simple Arithmetic Mean, Given array-like object: data"""
    return total(data) / len(data)

def deviation(data):
    """
    Returns list of deviations from mean, given array-like object: data
    """
    data_mean = mean(data)
    return [x - data_mean for x in data]

def deviation_squared(data):
    """
    Returns a list of squared-deviations from the mean, given array-like object: data
    """
    return [x**2 for x in deviation(data)]

def cross_product(data_1, data_2):
    """
    Returns a list of cross-proucts of deviations from two sets of data.
    Given x2 array-like objects with same n number of elements
    """
    return [x * y for x, y in zip(deviation(data_1), deviation(data_2))]

def variance(data):
    """
    Calculates the variance with (n-1) degrees of freedom.
    Given an array-like object: data
    """
    return total( deviation_squared(data) ) / (len(data) - 1)

def covarriance(data_1, data_2):
    """
    Calculates the covarriance of two data sets with (n-1) degrees of freedom.
    Given x2 array-like objects: data_1 and data_2
    """
    return total( cross_product(data_1, data_2) ) / (len(data_1) - 1)

def simp_linear_regression_slope(data_1, data_2):
    """
    Calculates the slope, or Beta-1, in a simple linear regressional model
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    return covarriance(data_1, data_2) / variance(data_1)

def simp_linear_regression_intercept(data_1, data_2):
    """
    Calculates the intercept, or Beta-0, in a simple linear regressional model
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    slope = simp_linear_regression_slope(data_1, data_2)
    intercept = mean(data_2) - slope * mean(data_1)
    return intercept

def simp_linear_regression(data_1, data_2):
    """
    Gives Intercept and Slope of a Simple Linear Regression model.
    Beta-0 and Beta-1
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    return (
        simp_linear_regression_intercept(data_1, data_2), 
            simp_linear_regression_slope(data_1, data_2)
           )
    
def regres(data_1, data_2):
    """
    Calculates a paired regression line that can be used for plotting later.
    """
    model_par = simp_linear_regression(data_1, data_2)
    intercept = model_par[0]
    slope = model_par[1]
    x_hat = [x for x in range( round(min(data_1)) - 2, round(max(data_1)) + 2, round(len(data_1)*.25))]
    y_hat = [intercept + slope * x for x in x_hat]
    return (x_hat, y_hat)
    
def y_hat(data_1, data_2):
    """
    Returns a list of estimated Y-values from a simple linear regression model.
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    model_param = simp_linear_regression(data_1, data_2)
    intercept = model_param[0]
    slope = model_param[1]
    model_run = lambda x: intercept + slope * x
    return list(map(model_run, data_1))

def deviation_error(data_1, data_2):
    """
    Returns a list of error-values from a simple linear regression model.
    ie. the Deviation of (Y-Actual - Y-Estimated)
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    y_act = np.array(data_2)
    y_ht = np.array( y_hat(data_1, data_2))
    return y_act - y_ht

def deviation_error_sq(data_1, data_2):
    """
    Returns a list of squared error-values from a simple linear regression model.
    ie. the squared Deviation of (Y-Actual - Y-Estimated)
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    return deviation_error(data_1, data_2) ** 2

def rss(data_1, data_2):
    """
    Returns the Residual Sum of Squares
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    return sum( deviation_error_sq(data_1, data_2) )

def mse(data_1, data_2):
    """
    Returns the Mean Squared Error assuming (n-k) degrees of freedom
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    n = len(data_1)
    return rss(data_1, data_2) / (n-2)

def se_beta_0(data_1, data_2):
    n = len(data_1)
    mse_y = mse(data_1, data_2)
    sum_dev_x = sum(deviation_squared(data_1))
    sq_mean = mean(data_1) ** 2
    df_x = 1/n
    return (mse_y * (df_x + sq_mean / sum_dev_x)) ** (1/2)

def se_slope(data_1, data_2):
    return ( mse(data_1, data_2) / sum(deviation_squared(data_1)) ) ** (1/2)

def t_stat_beta_0(data_1, data_2):
    beta_0 = simp_linear_regression_intercept(data_1, data_2)
    se_b_0 = se_beta_0(data_1, data_2)
    return beta_0 / se_b_0

def t_stat_beta_1(data_1, data_2):
    beta_1 = simp_linear_regression_slope(data_1, data_2)
    std_er = se_slope(data_1, data_2)
    return beta_1/std_er

def r_sq(data_1, data_2):
    """
    Returns the R-Squared Value
    Given x2 array-like objects: data_1 and data_2
    Where Data_1 is the independent variable on the x-axis
    """
    y_hats = y_hat(data_1, data_2)
    return total( deviation_squared( y_hats) ) / total( deviation_squared( data_2))

def adj_r_sq(data_1, data_2):
    n = len(data_1)
    k = 1 # later K could be the number of independent variables
    r_sq2 = r_sq(data_1, data_2)
    df = n - 1
    df_k = n - k - 1

    return 1 - (
    (1-r_sq2)*df
    /
    df_k
    )


def simple_linear_regression(data_1, data_2, xlabel="Independent Variable", ylabel="Dependent Variable"):
    import matplotlib.pyplot as plt
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.grid(True, color='deeppink', alpha=0.5)
    ax.set_xlabel(xlabel, color='deeppink')
    ax.set_ylabel(ylabel, color='deeppink')
    ax.tick_params(axis='x', colors='deeppink')
    ax.tick_params(axis='y', colors='deeppink')
    for spine in ax.spines.values():
        spine.set_edgecolor('deeppink')
    
    ax.scatter(data_1, data_2, c='deeppink', alpha=0.5)
    line = regres(data_1, data_2)
    ax.plot(line[0], line[1], color='deeppink', linewidth=2)
    plt.show()
