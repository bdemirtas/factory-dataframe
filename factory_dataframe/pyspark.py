import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

from factory_dataframe.base import Factory

spark = SparkSession.builder.getOrCreate()


class PySparkDataFrameFactory(Factory):
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

        if all(not v for v in cls.data.values()):
            return spark.createDataFrame([], StructType([]))
        return spark.createDataFrame(df)
