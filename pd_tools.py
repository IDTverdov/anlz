import pandas as pd
import matplotlib.pyplot as plt


class PdTools(object):
    def __init__(self):
        super(PdTools, self).__init__()

    def get_data(self, result):
        df = pd.DataFrame(result)
        data = df['balance_first']
        return data

