"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Elijah Williams.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk

def print_hello():
    print('hello')

def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # TODO: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()





    # ------------------------------------------------------------------
    # TODO: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding = 10)
    frame1.grid()
    # ------------------------------------------------------------------
    # TODO: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button1 = ttk.Button(root, text='Hi!')
    button1.grid()
    # ------------------------------------------------------------------
    # TODO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button1['command'] = (lambda:
                          print_hello())
    button1.grid()

    # ------------------------------------------------------------------
    # TODO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry_box = ttk.Entry(frame1)
    entry_box.grid()
    entry_button = ttk.Button(frame1, text='Print Entry')
    entry_button['command'] = (lambda:
                            print_entry(entry_box))
    entry_button.grid()
    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry_box2 = ttk.Entry(frame1)
    entry_box2.grid()
    entry_button2 = ttk.Button(frame1, text='Print Entry Multiple')
    entry_button2['command'] = (lambda:
                                print_many(entry_box, entry_box2))
    entry_button2.grid()
    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
def print_entry(entry_box):
    entry = entry_box.get()
    print(entry)
def print_many(entry_box, n):
    s = n.get()
    n = int(s)
    entry = entry_box.get()
    for k in range(n):
        print(entry)
main()
