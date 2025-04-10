def present_value(future_value, interest_rate, time_periods):
    """
    Computes Present Value.
    Given Future_value
    Interest_rate per period expressed as decimalized %, ie. 8% = 0.08
    Time_Periods. Note: Time_Period has to be consistent with interest-rate period.
    """
    return future_value * (1 + interest_rate) ** (-time_periods)
def future_value(present_value, interest_rate, time_periods):
    """
    Computes Future Value
    Given Present_Value
    Interest_rate per period expressed as decimalized %, ie. 8% = 0.08
    Time_Periods. Note: Time_Period has to be consistent with interest-rate period.
    """
    return present_value * (1 + interest_rate) ** time_periods

def interest_rate(future_value, present_value, time_periods):
    """
    Computes interest_rate, or growth_rate
    Given Future_value
    Present_value
    Then given the number of time periods between present-future value
    """
    return (future_value / present_value)** (1/time_periods) -1

def fv_annuity(annuity, interest_rate, time_periods, due=False):
    """
    Computes the future-value of a stream of equal cash_flows
    Given annuity amount
    Given interest_rate
    Given time_periods
    """
    if due == True:
        return annuity * (( (1 + interest_rate) ** time_periods - 1) / interest_rate) * (1 + interest_rate)
    return annuity * (( (1 + interest_rate) ** time_periods - 1) / interest_rate)

def pv_annuity(annuity, interest_rate, time_periods, due=False):
    """
    Computes the present-value of a stream of equal cash_flows
    Given annuity amount
    Given interest_rate
    Given time_periods
    """
    if due == True:
        return annuity * ( (1 - ( 1 / (1 + interest_rate) ** time_periods ) ) / interest_rate) * (1+interest_rate)
    return annuity * ( (1 - ( 1 / (1 + interest_rate) ** time_periods ) ) / interest_rate)

def payment_annuity(present_value, interest_rate, time_periods):
    """
    Computes the size of Annuity Payment
    Given the present_value
    The Interest Rate
    Number of Payment Periods
    Assuming Future Value of zero
    """
    fv_factor = (1 + interest_rate)**time_periods
    pv_factor = 1 / fv_factor
    pv_factor_numer = 1 - pv_factor
    annuity_payment_factor = pv_factor_numer / interest_rate
    annuity_payment = present_value / annuity_payment_factor
    return annuity_payment

def payment_fv_annuity(future_value, interest_rate, time_periods):
    """
    Computes the Payment Amount Needed to Acheive a Future Value
    Given Future Value,
    Interest Rate,
    Number of Time Periods
    Assuming Present Value of Zero
    """
    from TVM_Beginner import present_value
    pv = present_value(future_value, interest_rate, time_periods)
    return payment_annuity(pv, interest_rate, time_periods)

def growing_annuity(annuity, discount_rate, growth_rate, time_periods):
    """
    Computes the Present Value of a Growing Annuity Payment
    Given the Annuity payment Amount
    The Discount Rate
    The Growth Rate
    Number of Time Periods
    """
    net_rate = discount_rate - growth_rate
    annuity_factor = (1 - ((1.03/1.10)**time_periods))
    return annuity / net_rate * annuity_factor

def perpetuity_pv(annuity, interest_rate, due_date=0):
    """
    Returns the Present-Value of a Perpetuity, a level cash-flow paid in perpetuity
    Given Annuity amount,
    Interest-Rate
    Due-Date
    """
    if due_date == 0:
        return annuity / interest_rate
    else:
        return present_value( (annuity / interest_rate), interest_rate, due_date-1) 

def ear(apy, compound=12):
    """Returns Effective Annual Rate given APY in decimalized form (ie. .20 = 20%)
    Assumes Monthly-Compounding
    """
    return ( (1 + apy/compound) ** compound) - 1

def irr(cash_flows, discount_rate):
    """Returns the Internal Rate of Return
    Given a series of cash-flows, represented as an array or list.
    Given a Discount Rate in decimalized percent.
    """
    def time_line(cash_flows):
        return [x for x in range(0, len(cash_flows))]
    
    return sum( [present_value(x, discount_rate, y) for x, y in zip(cash_flows, time_line(cash_flows) )] )