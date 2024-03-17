import tkinter as tk
import random
def generate_random_colors():
    for i in range(5):
        # Generate random RGB values
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Create a label to display the RGB values
        color_label = tk.Label(root, text="", bg=f"#{r:02x}{g:02x}{b:02x}",width=29,height=130)
        color_label.place(x=i*218,y=100)
        #displaying rgb values
        font1=("ariel",11,"bold italic")
        c1=tk.Label(root,text=f"R : {r}\n G : {g}\n B : {b}",bg=f"#{r:02x}{g:02x}{b:02x}",font=font1)
        c1.place(x=i*218,y=470)
        

# Create the main application window
root = tk.Tk()
#font for button
custom_font = ("Georgia", 15, "bold italic")
#main window styling
root.title("Colors Generator")
root.configure(background='white')
root.geometry("1000x1000")

# Create a button to generate random colors
generate_button = tk.Button(root, text="Generate", command=generate_random_colors,width=15,height=2,font=custom_font, bg="#132f55",fg="white")
generate_button.place(x=500,y=25)

# Run the Tkinter event loop
root.mainloop()
