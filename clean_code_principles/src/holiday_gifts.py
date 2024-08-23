"""
Module for compute_total_price function.

Author: David Damián
Date: August, 2023
"""
import time
import numpy as np

def compute_total_price_gifts(gift_costs_path):
    """
    Compute the total cost (after taxes) of gifts whose value
    are less than 25 dollars.
    ----------------------------------------------------------
    Inputs:
    -------
        * gift_costs_path (str) : data path of gift costs
    Outputs:
    --------
        * total_price (float): Sum of prices after taxes
    """

    with open(gift_costs_path, encoding = 'utf-8') as file_path:
        gift_costs = file_path.read().split('\n')

    # store gift costs in numpy array
    gift_costs = np.array(gift_costs).astype(int)
    # filter gift which value is less than 25
    # and sum its values. Then add taxes
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
    return total_price

if __name__ == "__main__":
    # define the path where data is stored
    DATA_PATH = 'gift_costs.txt'
    start = time.time()
    # compute total price
    total_price_ = compute_total_price_gifts(
        gift_costs_path = DATA_PATH)
    execution_time = time.time() - start
    print(f'Duration: {execution_time} seconds')
    print(total_price_)
    