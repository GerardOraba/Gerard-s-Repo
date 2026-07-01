from abc import ABC, abstractmethod
 
# Abstract Class (Abstraction)
class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # Encapsulation (Private Attribute)
 
    # Getter Method
    def get_isbn(self):
        return self.__isbn
 
    # Setter Method
    def set_isbn(self, isbn):
        if isbn:
            self.__isbn = isbn
 
    @abstractmethod
    def display_info(self):
        pass
 
    @abstractmethod
    def to_dict(self):
        # Each subclass must define how to convert itself to a dictionary for JSON
        pass
 