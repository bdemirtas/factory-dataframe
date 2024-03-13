from pyspark.sql import SparkSession

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
        pass
