from abc import ABC, abstractmethod

# Abstract Class (Abstraction)
class Book(ABC):     # (                   )   "Parameter"                     
    def __init__(self, title, author, isbn):                            
        self.title = title                                            #] "Private Variable"
        self.author = author                                          #]
        self.__isbn = isbn  # Encapsulation (Private Attribute)        ]

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        if isbn:
            self.__isbn = isbn

    @abstractmethod
    def display_info(self):
        pass


