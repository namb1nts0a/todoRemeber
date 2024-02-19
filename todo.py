from dataclasses import dataclass
from datetime import date

@dataclass
class Todo:
    list_task: list 
    type_todo: str 
    validite_todo: date

    def get_list_task(self):
        return self.list_task
    
    def get_type_todo(self):
        return self.type_todo
    
    def get_validite_todo(self):
        return self.validite_todo
    
    def add_todo(self, new_task):
        self.list_task.append(new_task)

    def set_type_todo(self, new_type_todo):
        self.type_todo = new_type_todo

    def set_validation_todo(self, date_fin):
        self.validite_todo = date_fin

