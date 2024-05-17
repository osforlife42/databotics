from typing import Any
from enum import Enum

class CustomDataPoolTypes(Enum): 
    NO_NEW_DATA = 1

class DataPool(): 
    def __init__(self) -> None:
        self.__data_pool = dict()
        self.write_elements = dict() 
        self.read_elements = dict()
        pass

    def register_write_element(self, key: str, element_name: str):
        if self.write_elements.get(key): 
            raise Exception(f"invalid for more than one element to write to the same key. {element_name} and {self.write_elements.get(key)}")  
        self.write_elements[key] = element_name

    def register_read_element(self, key, element_name: str): 
        if self.write_elements.get(key): 
            raise Exception(f"invalid to read key which no element writes to. element {element_name} trying to read from key: {key}") 
        self.read_elements[key] = element_name 

    def get_data(self, key: str) -> Any:
        pass 

    def write_data(self, key: str, value: Any): 
        pass 


