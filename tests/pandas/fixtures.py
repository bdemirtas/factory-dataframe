import pytest

from factory_dataframe.pandas import PandasDataFrameFactory
from tests.fixtures import SimpleModel


@pytest.fixture
def simple_factory_model(faker):
    class SimplePandasFactoryModel(PandasDataFrameFactory):
        class Meta:
            model = SimpleModel

        first_name = faker.first_name
        last_name = faker.last_name
        date = faker.date

    return SimplePandasFactoryModel
