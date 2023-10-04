
from tkinter import * 
from cell import Cell
import settings
import utils
import sqlite3

conn = sqlite3.connect('data_base.db')

# Override the settings of the windows
root=Tk() # Widget creation (windows)
root.configure(bg="black") # background config
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')#dimensions config
root.title("Minesweeper Game")
root.resizable(False,False) # delete window modification


# class fram() with different possible settings
top_frame=Frame( 
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.HEIGHT_prct(25),# dim config with percentage of settigns
    )

# .place() methode for widgets position
top_frame.place(x=0,y=0)

left_frame=Frame(
    root,
    bg='black',
    width=utils.WIDTH_prct(25),
    height=utils.HEIGHT_prct(75))

left_frame.place(x=0, y=utils.HEIGHT_prct(25))

center_frame= Frame(
    root,
    bg='black',
    width=utils.WIDTH_prct(75),
    height=utils.HEIGHT_prct(75)
)

center_frame.place(x=utils.WIDTH_prct(25),
                   y=utils.HEIGHT_prct(25)
)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utils.WIDTH_prct(25), y=0
)
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y) 

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)
Cell.randomize_mines()


#Run the Windows
root.mainloop() # An infinite loop

