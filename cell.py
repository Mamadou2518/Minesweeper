# -*- coding: utf-8 -*-
import sys
from tkinter import Button, Label
import settings
import random
import ctypes
import sys


class Cell:
    all = [] #empty list for all created cells
    cell_count=settings.CELL_COUNT
    cell_count_label= None
    def __init__(self,x,y,is_mine = False,is_opened=False,is_mine_candidate=False): # method called every time an object is created from a class
        self.is_mine = is_mine
        self.is_opened= is_opened
        self.is_mine_candidate= is_mine_candidate
        self.cell_btn_object = None #creation of a button object
        self.x=x
        self.y=y   

        #Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self,location):
        btn = Button(
            location,
            width=settings.BUTTON_WIDTH,
            height=settings.BUTTON_HEIGHT,
        
        )
        btn.bind('<Button-1>',self.left_click_actions) #bind fct for events and button -1 left click
        btn.bind('<Button-3>',self.right_click_actions)#button -3 covention for right click 
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left: {Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl


    def left_click_actions(self,event):
        if self.is_mine: #if is_mine== true
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length ==0:
                #show automatiquely surrounded cells if there is no mines surround
                for cell_object in self.surrounded_cells:
                    cell_object.show_cell()
            self.show_cell()
        # Cancel Left and Right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
        # If Mines count is equal to the cells left count, player won
        if Cell.cell_count == settings.MINES_COUNT:
            ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)
            sys.exit()

    
    def get_cell_by_axis(self,x,y):
        #return a cell object based on the values of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y :
                return cell

    @property
    def surrounded_cells (self):
        cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
        ]
        #comprehension list to delete cells with None values
        cells = [cell for cell in cells if cell is not None] 
        return cells

    @property
    def surrounded_cells_mines_length(self):
        #calculate how many mines are there surround cells
        counter=0 
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter +=1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
          # Replace the text of cell count label with the newer count
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(
                text=f"Cells Left:{Cell.cell_count}")
        # Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True
        # If this was a mine candidate, then for safety, we should
        # configure the background color to SystemButtonFace
        self.cell_btn_object.configure(
            bg='SystemButtonFace')

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0) #display a message for the user
        sys.exit()# exit the game
    
    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='orange')
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace' #default color of the buttom
            )
            self.is_mine_candidate=False



    @staticmethod
    #static method to change attribute is_mine in to true
    def randomize_mines():
        picked_cells = random.sample(Cell.all,settings.MINES_COUNT)
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    def __repr__(self) -> str:
        return f"cell({self.x},{self.y})"

