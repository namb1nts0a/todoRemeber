from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:

    name_task: str
    begin_task: datetime
    urgent: bool

    def get_name_task(self):
        return self.name_task
    
    def get_begin_task(self):
        return self.begin_task
    
    def get_urgent(self):
        return self.urgent
    
    def set_name_task(self, new_name):
        self.name_task = new_name

    def set_begin_task(self, new_begin):
        self.begin_task = new_begin

    def set_urgent(self, new_urgent): 
        self.urgent = new_urgent