import numpy as np
import pytest

from factory_dataframe.pyspark import PySparkDataFrameFactory
from tests.fixtures import SubFactorySimpleModel


@pytest.mark.parametrize("nbrow", [(0), (15), (100)])
def test_create_dataframe(check, simple_factory_model, nbrow):
    df = simple_factory_model.create(size=nbrow)
    check.equal(df.count(), nbrow)


def test_create_with_random_na(check, simple_factory_model):
    df = simple_factory_model.create(perc_na=0.2).toPandas()
    check.is_true(df.isnull().any().any())


def test_create_with_zero_random_na(check, simple_factory_model):
    df = simple_factory_model.create(perc_na=0.0).toPandas()
    check.is_false(df.isnull().any().any())


def test_create_with_random_column_na(check, simple_factory_model):
    df = simple_factory_model.create(
        columns=["last_name"], perc_na=0.2
    ).toPandas()
    check.is_true(df["last_name"].isnull().any())


def test_create_with_list_values(check, faker, simple_factory_model):
    df_simple = simple_factory_model.create()

    class SubFactorySimpleModelFactory(PySparkDataFrameFactory):
        class Meta:
            model = SubFactorySimpleModel

        first_name = faker.first_name
        last_name = faker.last_name
        date = faker.date

    expected_df = SubFactorySimpleModelFactory.create(
        first_name=[row["first_name"] for row in df_simple.collect()],
        last_name=[row["last_name"] for row in df_simple.collect()],
        date=[row["date"] for row in df_simple.collect()],
    )
    check.equal(df_simple.intersect(expected_df).count(), 10)
