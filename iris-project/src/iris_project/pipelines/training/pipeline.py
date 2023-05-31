"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_model,evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=train_model,
             inputs=["X_train", "y_train","params:model_params"],
             outputs="model"),
        node(func=evaluate_model,
             inputs=["model","X_test", "y_test"],
             outputs=None)])
