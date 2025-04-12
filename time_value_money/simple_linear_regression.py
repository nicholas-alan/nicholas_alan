import numpy as np

def total(data):
    sum_data = 0
    for x in data:
        sum_data += x
    return sum_data

def mean(data):
    return total(data) / len(data)

def deviation(data):
    data_mean = mean(data)
    return [x - data_mean for x in data]

def deviation_squared(data):
    return [x**2 for x in deviation(data)]

def cross_product(data_1, data_2):
    return [x * y for x, y in zip(deviation(data_1), deviation(data_2))]

def variance(data):
    return total( deviation_squared(data) ) / (len(data) - 1)

def covarriance(data_1, data_2):
    return total( cross_product(data_1, data_2) ) / (len(data_1) - 1)

def simp_linear_regression_slope(data_1, data_2):
    """Where Data_1 is the independent variable on the x-axis"""
    return covarriance(data_1, data_2) / variance(data_1)

def simp_linear_regression_intercept(data_1, data_2):
    slope = simp_linear_regression_slope(data_1, data_2)
    intercept = mean(data_2) - slope * mean(data_1)
    return intercept

def simp_linear_regression(data_1, data_2):
    return (simp_linear_regression_intercept(data_1, data_2), 
            simp_linear_regression_slope(data_1, data_2)
           )
def regres(data_1, data_2):
    model_par = simp_linear_regression(data_1, data_2)
    intercept = model_par[0]
    slope = model_par[1]
    x_hat = [x for x in range( round(min(data_1)) - 2, round(max(data_1)) + 2, round(len(data_1)*.25))]
    y_hat = [intercept + slope * x for x in x_hat]
    return (x_hat, y_hat)
    
def y_hat(data_1, data_2):
    model_param = simp_linear_regression(data_1, data_2)
    intercept = model_param[0]
    slope = model_param[1]
    model_run = lambda x: intercept + slope * x
    return list(map(model_run, data_1))

def deviation_error(data_1, data_2):
    y_act = np.array(data_2)
    y_hat = np.array(y_hat(data_1, data_2))
    return y_act - y_hat

def deviation_error_sq(data_1, data_2):
    return deviation_error(data_1, data_2) ** 2

def rss(data_1, data_2):
    return sum( deviation_error(data_1, data_2) ** 2 )

def mse(data_1, data_2):
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
    model_par = simp_linear_regression(data_1, data_2)
    intercept = model_par[0]
    slope = model_par[1]
    model_eq = lambda x: intercept + slope * x
    y_hat = [model_eq(x) for x in data_1]
    return total( deviation_squared( y_hat) ) / total( deviation_squared( data_2))

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
