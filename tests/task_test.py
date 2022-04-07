import unittest

from src.task import *
from src.get_prefered import *

class TestTask(unittest.TestCase):
    def setUp(self): 
        self.task_1 = Task("Wash Dishes", 10)
        self.task_2 = Task("Cook Dinner", 30)
        self.task_3 = Task ("Clean Windows", 60)


    def test_wash_dish_has_description (self):
        self.assertEqual("Wash Dishes", self.task_1.description)
    
    def test_wash_dish_has_duration (self):
        self.assertEqual(10, self.task_1.duration)


    def test_wash_dish_perfered_over_cook_dinner(self):
        task = get_prefered(self.task_1, self.task_2)
        self.assertEqual("Wash Dishes", task.description)

    def test_cook_dinner_perfered_over_clean_windows(self):
        task = get_prefered(self.task_2, self.task_3)
        self.assertEqual("Cook Dinner", task.description)
    
    def test_clean_windows_perfered_over_wash_dish(self):
        task = get_prefered(self.task_3, self.task_1)
        self.assertEqual("Clean Windows", task.description)
    

    
