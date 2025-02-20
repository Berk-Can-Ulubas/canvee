from model.base import Base
from model.color import Color
from model.home import Home
from model.space import Space
from model.start import Start


class Board:
    def __init__(self):
        self.NUMBER_OF_SPACES = 36
        self.HOLDERS_PER_HOME = 4
        self.HOLDERS_PER_BASE = 4
        self.SPACES_BETWEEN_STARTS = 9
        self.NUMBER_OF_BASES = 4
        self.NUMBER_OF_STARTS = 4
        self.NUMBER_OF_HOMES = 4

        #create graph for the board
        self.adjacency_list =[]
        #create the spaces
        for i in range(self.NUMBER_OF_SPACES):
            self.adjacency_list.append(Space(i))
        #create the start holders
        for color in Color:
            self.adjacency_list.append(Start(color))
        #create the bases
        for color in Color:
            for i in range(self.HOLDERS_PER_BASE):
                self.adjacency_list.append(Base(color, i))
        #create the homes
        for color in Color:
            for i in range(self.HOLDERS_PER_HOME):
                self.adjacency_list.append(Home(color, i))
        #create edges
        self.connect_spaces()
        #connect starts to spaces
        self.connect_starts()

    def connect_spaces(self):
        for i in range(self.NUMBER_OF_SPACES, 1, -1):
            if (i % self.SPACES_BETWEEN_STARTS) == 0:
                self.adjacency_list[i].set_next_holder(None)
            else:
                self.adjacency_list[i].set_next_holder(self.adjacency_list[i-1])
        

    def connect_starts(self):
        self.STARTS_INDEX = self.NUMBER_OF_SPACES + 1
        #blue
        self.adjacency_list[self.STARTS_INDEX].set_next_holder(self.adjacency_list[0]) #holder after blue start
        #yellow
        self.adjacency_list[self.SPACES_BETWEEN_STARTS].set_next_holder(self.adjacency_list[self.STARTS_INDEX +1]) #holder before yellow start
        self.adjacency_list[self.STARTS_INDEX + 1].set_next_holder(self.adjacency_list[self.SPACES_BETWEEN_STARTS + 1]) #holder after yellow start
        #green
        self.adjacency_list[2*self.SPACES_BETWEEN_STARTS].set_next_holder(self.adjacency_list[self.STARTS_INDEX +2]) #holder before green start
        self.adjacency_list[self.STARTS_INDEX + 2].set_next_holder(self.adjacency_list[2*self.SPACES_BETWEEN_STARTS +1]) #holder after green start
        #red
        self.adjacency_list[3*self.SPACES_BETWEEN_STARTS].set_next_holder(self.adjacency_list[self.STARTS_INDEX + 3]) #holder before red start
        self.adjacency_list[self.STARTS_INDEX + 3].set_next_holder(self.adjacency_list[3*self.SPACES_BETWEEN_STARTS +1]) #holder after red start
        #blue
        self.adjacency_list[4*self.SPACES_BETWEEN_STARTS].set_next_holder(self.adjacency_list[self.STARTS_INDEX]) #holder before blue start
    
    def connect_bases(self):
        self.BASES_INDEX = self.STARTS_INDEX + self.NUMBER_OF_STARTS
        for i in range(self.BASES_INDEX , self.BASES_INDEX + self.HOLDERS_PER_BASE * self.NUMBER_OF_BASES, self.HOLDERS_PER_BASE):
            for j in range(self.HOLDERS_PER_BASE):
                self.adjacency_list[i+j].set_next_holder(self.adjacency_list[self.STARTS_INDEX + self.adjacency_list[i+j].get_color().value])
    
    def connect_homes(self):
        self.HOMES_INDEX = self.BASES_INDEX + self.NUMBER_OF_BASES * self.HOLDERS_PER_BASE
        for i in range(self.HOMES_INDEX, self.HOMES_INDEX + self.HOLDERS_PER_HOME * self.NUMBER_OF_HOMES, self.HOLDERS_PER_HOME):
            for j in range(self.HOLDERS_PER_HOME):
                self.adjacency_list[i+j].set_next_holder(self.adjacency_list[self.BASES_INDEX + self.adjacency_list[i+j].get_color().value * self.HOLDERS_PER_BASE])


