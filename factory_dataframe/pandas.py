import numpy as np
import pandas as pd

from factory_dataframe.base import Factory


class PandasDataFrameFactory(Factory):
    class Meta:
        abstract = False
        model = None

    @classmethod
    def _create(
        cls,
        size=10,
        perc_na=None,
        **kwargs,
    ):
        df = pd.DataFrame(columns=cls.columns_name, data=cls.data)
        if perc_na:
            mask = np.random.choice(
                [True, False], size=df.shape, p=[perc_na, 1 - perc_na]
            )
            df = df.mask(mask)
        return df
