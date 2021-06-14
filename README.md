<!--Head-->
# vix_strategy_backtest

![Logo](https://github.com/ArunavD/vix_strategy_backtest/blob/master/Figure_0.png)

### Fearful when others are greedy, and greedy when others are fearful.




## Contents

* [What is Vix strategy?](#What-is-Vix-strategy)
* [The strategy I have used](#The-strategy-I-have-used)
* [Libraries](#Libraries)
* [Description of each file](#Description-of-each-file)
* [Datasets](#Datasets)
* [How to use?](#How-to-use)


## What is Vix strategy?

The [VIX index](https://www.cboe.com/tradable_products/vix/), also known as the “fear index” is reported by the Chicago Board Options Exchange and provides investors and traders valuable insight into current greed and fear levels in the market. 
The Cboe Volatility Index (VIX) is a real-time index that represents the market's expectations for the relative strength of near-term price changes of the S&P 500 index (SPX).


## The strategy I have used

First of all I have ploted both the graph of s&p500 and vix index. According the the plotted graph, I have decided that whenever vix index hit 35 or more i will buy the shares as fear is in market.
Then I have tested by selling the shares whenever vix index hit 10. But result was not so good.
Then I have created a strategy where I will add 5000$ of cash to the broker at every 20 days or one market month. And buy stocks only when vix index hit 35. This gave a preety nice result.



<!-- Libraries -->
## Libraries

+ [backtrader](https://www.backtrader.com) - It is an open-source framework that allows for strategy testing on historical data.
+ [pandas](https://pypi.org/project/pandas/) - the most powerful and flexible open source data analysis / manipulation tool.
+ [os](https://www.geeksforgeeks.org/os-module-python-examples/) - The OS module in Python provides functions for interacting with the operating system.
+ [DateTime](https://pypi.org/project/DateTime) - This module supplies classes for manipulating dates and times.



<!-- Description -->
## Description of each file

1. [main.py](https://github.com/ArunavD/vix_strategy_backtest/blob/master/main.py) - This is the main method of the project where strategy is being executed with the help of backtrader's cerebro method.
2. [VIXStrategy.py](https://github.com/ArunavD/vix_strategy_backtest/blob/master/VIXStrategy.py) - Here I have created the strategy to implement the VIX index in S&P500.



## Datasets

I have downloaded the [S&P500](https://github.com/ArunavD/vix_strategy_backtest/blob/master/spy.csv) amd [VIX](https://github.com/ArunavD/vix_strategy_backtest/blob/master/vix.csv) datasets and combine the to use my strategy as [SPY_VIX.csv](https://github.com/ArunavD/vix_strategy_backtest/blob/master/spy_vix.csv).
Other stocks historical data also can be downloaded from [yahoo finance](https://in.finance.yahoo.com/).


