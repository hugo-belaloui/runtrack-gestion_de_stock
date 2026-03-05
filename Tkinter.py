import tkinter  # Import the tkinter module, which contains the tools to build the Graphical User Interface (GUI)

window = tkinter.Tk()  # Create the main window instance, this is the container for all other widgets
window.title("Store")  # Set the text that appears in the title bar of the window
window.geometry("1500x700")  # Set the initial size of the window in pixels (width x height)


label = tkinter.Label(window, text="STORE'S DASHBOARD", font=("Arial", 40), bg="#2B8D19")
label.pack(side="top", ipady=30, fill="both")


window.mainloop()  # Start the event loop. This keeps the window open and listening for events (like clicks or key presses) until closed