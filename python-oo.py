"""python serial Number Generator"""
class SerialGenerator:
    
    def __init__(self, start=0):
        """initializer to create serial numbers from a given start point
        >>> serial = SerialGenerator(start=100)
        start: 100 ... next: 100

        >>> serial.generate()
        100

        >>> serial.generate()
        101

        >>> serial.reset()
        

        >>> serial.generate()
        100
        
        """
        self.start = self.next = start
        print(f"start: {self.start} ... next: {self.next}")
    
    def generate(self):
        """actual serial generator that is called and gives increments of 1 from the start number"""
        self.next +=1
        return(self.next -1)

    def __repr__(self):
        """function that allows the user to see where the current serial number is and what is the current start number"""
        print(f"start: {self.start}.....next: {self.next}")

    def reset(self):
        """function that resets the serial number to the start number , the start number stays the same"""
        self.next = self.start

    

import random

class WordReader:
    """this is a class for a word reader/finder generator , that reads over a file and gives 
    back amount of words read and has functions that you can use to get a random word

    >>> wordFile = WordReader("words.txt")
    235886 words read

    
    
    """

    """this is the initializer that reads over and parses a file"""
    def __init__(self,fileName):
        file = open(fileName)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")
    
    """this is a function that parses a file and puts it into a list"""
    def parse(self,fileName):
        return[w.strip() for w in fileName]

    """this is a method that gives back a random word from the parsed words"""
    def ramdomWord(self):
        return random.choice(self.words)



class SpecialWordFinder(WordReader):
    def parse(self,file):
        return[w.strip() for w in file if w.strip() and not w.startswith("#")]


