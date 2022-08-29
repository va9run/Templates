# Compare DataFrame
import pandas as pd
import numpy as np
import unittest
from pandas.testing import assert_frame_equal


class testmethod(unittest.TestCase):
    def test_df_equals_to_df1(self,):
        df2 = pd.read_parquet('UnitTestingDf1.parquet')
        df1 = df2.copy()
        return (assert_frame_equal(df2,df1))

# ALWAYS HAVE THE FUNCTION NAME START WITH test otherwise IT WILL IGNORE IT AND WON'T
# ANYTHING
# In Terminal run python -m unittest #NAMEOFTHEMODULE(_unitTesting)
# python -m unittest _unitTesting