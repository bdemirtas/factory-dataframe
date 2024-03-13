import pytest

from factory_dataframe.pandas import PandasDataFrameFactory
from tests.fixtures import SubFactorySimpleModel


@pytest.mark.parametrize("nbrow", [(0), (15), (100)])
def test_create_dataframe(check, simple_factory_model, nbrow):
    models = simple_factory_model.create(size=nbrow)
    check.equal(len(models), nbrow)


def test_create_with_random_na(check, simple_factory_model):
    df = simple_factory_model.create(perc_na=0.2)
    check.is_true(df.isnull().any().any())


def test_create_with_zero_random_na(check, simple_factory_model):
    df = simple_factory_model.create(perc_na=0.0)
    check.is_false(df.isnull().any().any())


def test_create_with_random_row_na(check, simple_factory_model):
    df = simple_factory_model.create(perc_row_na=0.2)
    check.is_false(df.isnull().any().any())


def test_create_with_random_col_na(check, simple_factory_model):
    df = simple_factory_model.create(perc_col_na=0.2)
    check.is_false(df.isnull().any().any())


def test_create_with_list_values(check, faker, simple_factory_model):

    df_simple = simple_factory_model.create()

    class SubFactorySimpleModelFactory(PandasDataFrameFactory):
        class Meta:
            model = SubFactorySimpleModel

        first_name = faker.first_name
        last_name = faker.last_name
        date = faker.date

    expected_df = SubFactorySimpleModelFactory.create(
        first_name=df_simple["first_name"].to_list(),
        last_name=df_simple["last_name"].to_list(),
        date=df_simple["date"].to_list()
    )
    check.is_true(df_simple.equals(expected_df))


def test_create_sub_df_with_na(check, faker, simple_factory_model):

    df_simple = simple_factory_model.create()

    class SubFactorySimpleModelFactory(PandasDataFrameFactory):
        class Meta:
            model = SubFactorySimpleModel

        first_name = faker.first_name
        last_name = faker.last_name
        date = faker.date

    df = SubFactorySimpleModelFactory.create(
        perc_na=0.2,
        first_name=df_simple["first_name"].to_list(),
        last_name=df_simple["last_name"].to_list(),
        date=df_simple["date"].to_list()
    )
    check.is_true(df.isnull().any().any())