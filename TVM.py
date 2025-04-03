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
    fv_factor = (1 + interest_rate)**time_periods
    pv_factor = 1 / fv_factor
    pv_factor_numer = 1 - pv_factor
    annuity_payment_factor = pv_factor_numer / interest_rate
    annuity_payment = present_value / annuity_payment_factor
    return annuity_payment

def payment_fv_annuity(future_value, interest_rate, time_periods):
    from TVM_Beginner import present_value
    pv = present_value(future_value, interest_rate, time_periods)
    return payment_annuity(pv, interest_rate, time_periods)