from abc import abstractmethod
from dataclasses import fields


class FactoryMetaClass(type):
    def __new__(mcs, class_name, bases, attrs):
        meta = attrs.pop("Meta", None)
        attrs["_meta"] = meta
        options = FactoryOptions()
        attrs["_options"] = options
        new_class = super().__new__(mcs, class_name, bases, attrs)
        options.construct_class(meta, attrs)
        return new_class


class BaseMeta:
    abstract = True
    model = None


class FactoryOptions:
    def __init__(self):
        self.meta = None
        self.columns = {}
        self.factory_params = None

    def construct_class(self, meta, attrs):
        self.meta = meta
        self.factory_params = attrs
        if meta.model:
            self.construct_columns()
            self.override_columns()

    def construct_columns(self):
        for attr in fields(self.meta.model):
            self.columns[attr] = attr.default

    def override_columns(self):
        columns = {}
        for param, default in self.factory_params.items():
            if not param.startswith("_"):
                columns[param] = default
        self.columns = columns

    def create_default_column_generator(self, default):
        if callable(default):
            return default
        return lambda: default


class BaseFactory:

    def __new__(cls, *args, **kwargs):
        """Would be called if trying to instantiate the class."""
        raise Exception("You cannot instantiate BaseFactory")

    @classmethod
    def create(
        cls,
        size=10,
        perc_na=None,
        perc_row_na=None,
        perc_col_na=None,
        **kwargs,
    ):
        cls.columns_name = list(cls._options.columns)
        cls.data = {}

        for attr, column_generator in cls._options.columns.items():
            if attr in kwargs:
                cls.data[attr] = kwargs[attr]
            else:
                cls.data[attr] = [column_generator() for _ in range(size)]

        return cls._create(
            size, perc_na, perc_row_na=None, perc_col_na=None, **kwargs
        )

    @classmethod
    @abstractmethod
    def _create(
        cls,
        size,
        perc_na,
        perc_row_na=None,
        perc_col_na=None,
        **kwargs,
    ):
        raise NotImplementedError


class Factory(BaseFactory, metaclass=FactoryMetaClass):
    class Meta(BaseMeta):
        pass
