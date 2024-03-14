import pytest

from factory_dataframe.pyspark import PySparkDataFrameFactory
from tests.fixtures import SimpleModel


@pytest.fixture
def simple_factory_model(faker):
    class SimplePandasFactoryModel(PySparkDataFrameFactory):
        class Meta:
            model = SimpleModel

        first_name = faker.first_name
        last_name = faker.last_name
        date = faker.date

    return SimplePandasFactoryModel
