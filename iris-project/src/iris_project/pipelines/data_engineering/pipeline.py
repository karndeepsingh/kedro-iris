"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocessing, split_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=preprocessing,
             inputs="iris_data",
             outputs=["X","Y"]),
        node(func=split_data,
             inputs=["X","Y","params:split"],
             outputs=["X_train", "X_test", "y_train", "y_test"])
    ])
