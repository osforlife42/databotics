from databotics_pipeline.data_pool import DataPool, CustomDataPoolTypes
from abc import abstractmethod, ABC
from typing import Any

class PipeElement(ABC): 
    def __init__(self, data_pool: DataPool, name: str) -> None:
        self.data_pool = data_pool
        self.name = name
        self.inputs_names = []
        self.output_names = None

    def register_read_element(self, key: str):
        self.data_pool.register_read_element(key)

    def register_write_element(self, key: str, use_namespace=False):
        if use_namespace: 
            key = self.ns_prefix() + key 
        self.data_pool.register_write_element(key, self.name)

    def get_data(self, input_name: str, ):
        new_data = self.data_pool.get_data(input_name)

    @abstractmethod
    def write_data(self, data, ):
        pass              
    

    def ns_prefix(self,): 
        return f"{self.name}/"
