import pytest


@pytest.mark.parametrize("nbrow", [(0), (15), (100)])
def test_create_dataframe(check,  nbrow):
    pass

def test_create_with_random_na(check):
    pass


def test_create_with_zero_random_na(check):
    pass


def test_create_with_random_row_na(check):
    pass


def test_create_with_random_col_na(check):
    pass


def test_create_with_list_values(check, faker):
    pass

def test_create_sub_df_with_na(check, faker):
    pass