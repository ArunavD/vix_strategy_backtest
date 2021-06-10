import backtrader as bt
import os
import pandas as pd


cerebro = bt.Cerebro()


cerebro.broker.setcash(100000)


class SPYVIXData(bt.feeds.GenericCSVData):
    lines = ('vixopen' , 'vixhigh' , 'vixlow' , 'vixclose',)


    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date' , 0),
        ('spyopen' , 1),
        ('spyhigh' , 2),
        ('spylow' , 3),
        ('spyclose' , 4),
        ('spyadjclose' , 5),
        ('spyvolume' , 6),
        ('vixopen' , 7),
        ('vixhigh' , 8),
        ('vixlow' , 9),
        ('vixclose' , 10)
    )


class VIXData(bt.feeds.GenericCSVData):

    params = (
        ('dtformat', '%m/%d/%Y'),
        ('date', 0),
        ('vixopen', 1),
        ('vixhigh', 2),
        ('vixlow', 3),
        ('vixclose', 4),
        ('volume', -1),
        ('openinterest', -1)
    )



spy_vix_csv_file = os.path.dirname(os.path.realpath(__file__)) + "/spy_vix.csv"    

vix_csv_file = os.path.dirname(os.path.realpath(__file__)) + "/vix.csv"

#spy_vix_csv_file = pd.read_csv("data_sets/spy_vix.csv")
#vix_csv_file = pd.read_csv("data_sets/vix.csv")



spyVixDataFeed = SPYVIXData(dataname = spy_vix_csv_file)
vixDataFeed = VIXData(dataname = vix_csv_file)

cerebro.adddata(spyVixDataFeed)
cerebro.adddata(vixDataFeed)




cerebro.run()
cerebro.plot(volume = False)