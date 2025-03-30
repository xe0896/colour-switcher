The way this documentation went wasn't how it should be since I wasn't documenting while creating the solution, there will still be some thought processes here and there for the solution but for the most part it will just be explaining the code.
## Introduction

This program takes in a `.png` file that has a white background and changes the colour of the background to make it look nicer when you want to use images for Anki or Obsidian or any other type of other program that could showcase an image. `numpy` was used to make the colour conversion more efficient rather then just doing the following:

```python
for x in range(height):
	for y in range(width):
		r, g, b = img.getPixel(x,y)
		# RGB logic..
```

Furthermore, instead of the terminal as an interface, `Tkinter` was used as a GUI to input some values that allows the user to suit their needs, there was also some considerations of showcasing the image to the user on the GUI so I used modules such as `Pillow` to showcase it easier as `Tkinter` and `Pillow` integrate nicely.
## Colour switching

The main idea of the colour switching was to invert the image, i.e: turn black into white and white into black, then we create a mask such that if a pixel's RGB is `0` then the mask is `True`, else `False`, then we apply this mask and when it finds a match it will replace the RGB with the given RGB by the user, this will effectively convert a white background to the users wanted background. 

The program for the colour conversion relied on imports, since they are heavily used, the following imports used where:

```python
import numpy as np
from PIL import Image
```

When using anything from `numpy` we use `np` as the namespace is now `np` from the `as` keyword, from the `Pillow` module since we only want the `Image` function we do `import Image`.

Before we start manipulating the image, we must first convert the file as the special `numpy` array and also check to see if there are any alpha channels in the file:

```python
img = Image.open(data) # data = x.png where x is file name
image_arr = np.array(img)
channels = image_arr.shape[2]
```

The reason we store the channels will become apparent soon but about the way we do it is by using `np.shape` which returns the dimensions of the array and if `channels == 4` then we can assume it has an alpha channel (RGBA)

```python
if channels == 4:
	inverted_arr = 255 - image_arr[:,:,:3]
	inverted_arr = np.clip(inverted_arr, 0, 255)
	inverted_arr = np.dstack([inverted_arr, image_arr[:,:,:3]])
else:
	inverted_arr = 255 - image_arr
	inverted_arr = np.clip(inverted_arr, 0, 255)
```

The first if-statement checks to see if the alpha channel is present, if this is the case we first invert the RGB channels and leave the alpha channel for now, we then use the `np.clip()` function to ensure that our values are in the range `0-255`, then we use `np.dstack()` which combines our inverted array with the alpha channel from the original array. If there is no alpha channel we can just invert the whole array.

```python
is_black = np.all(inverted_arr = [0, 0, 0, 255], axis = -1)
inverted_arr[is_black] = [r, g, b, 255]
Image.fromarray(inverted_array).save('output.png')
```

`is_black` is a mask that checks all the RGB values via `np.all()`, notice that we assume alpha is `255` as the alpha channel for majority of the tests done had alpha as `255` so it was just a lazy solution, `axis` ensures that we check individual pixels. 

The above code was in encapsulated in a function `def process(data, r, g, b):` where `r,g,b` are values given by the user via the GUI respectively.

## Tkinter GUI

`main.py` contains the GUI stuff to make it the logic separated and also since I wanted to learn how we can make two `.py` files use each other:

```python
import calc
```

The above was imported in `main.py` as the colour conversion stuff was located at `calc.py`, this allows us to access `calc.py` functions and variables, we could of done `from calc import process` as our function was named `process` but the aliasing that `import calc` gives us was helpful since we could do `calc.process()` and ensure no other modules that contained `process` clashed if we just done `process()`

```python
root = Tk()
root.title("Color Switcher")
```

This creates the application with the name 'Color Switcher' and we can interact this via the `root` object

```python
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
```

`Tkinter` uses the concepts of frames which are divided into grids and allow us to add labels or buttons on the grids:

![[Pasted image 20250330143036.png]]

We can use `(column,row)` notation to denote a place in the grid where we can add our buttons/labels, to initialize the main grid we do the following:

```python
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
```

This creates the `mainframe` which as padding (boundaries) and since its our first initialization we use `column = 0, row = 1`,  we also clarify that we want `sticky = (N,W,E,S)` which means we want the grid to use all `N,W,E,S` and lastly we configure the row and columns such that it fits everything when initialized.

The `mainframe` will be used as the parent frame and all the other frames will be inside this frame, one of which will be the input field which will have the frame name: `input_frame`:

```python
input_frame = ttk.Frame(mainframe)
input_frame.grid(column = 1, row = 1, columnspan = 4, sticky = W)
```

Below is a sketch of how the grid should look like and what each grid will contain since we want the input field to make it obvious what that input field will do:

![[output.png]]

```python
ttk.Label(input_frame, text = "R:").grid(column = 1, row = 1, sticky = W)
r = StringVar()
r_entry = ttk.Entry(input_frame, width = 7, textvariable = r)
r_entry.grid(column = 2, row = 1, padx = 5)

ttk.Label(input_frame, text="G:").grid(column=3, row=1, sticky=W)
g = StringVar()
g_entry = ttk.Entry(input_frame, width=7, textvariable=g)
g_entry.grid(column=4, row=1, padx=5)
  
ttk.Label(input_frame, text="B:").grid(column=5, row=1, sticky=W)
b = StringVar()
b_entry = ttk.Entry(input_frame, width=7, textvariable=b)
b_entry.grid(column=6, row=1, padx=5)
```

The above places a `ttk` label like `R:` or `G:`and stores the input as a `StringVar()` to get real-time values as the user enters there values, and we specify the location the input should be in the grid.

Now that the input fields have been created, we now have to work on the buttons. For now we will work on the following buttons:

- Calculate: Colour switch
- Open:  Open the file, allows us to copy
- Anki: Preset values to colour switch to Anki
- Obsidian: Preset values to colour switch to Obsidian

To do this we create a new frame: `button_frame`, this will hold all our buttons allowing us to place them in separate grids from the `input_frame`:

```python
button_frame = ttk.Frame(mainframe)
button_frame.grid(column = 1, row = 2, columnspan = 6, sticky = "ew")
```

Note that we make the `button_frame` locate at `(column=1, row=2)` whereas our `input_frame` is at `(column=1, row=1)`, allowing us to control the position of different grids.

To create the buttons we must specify what function to execute when we press the button, we can also specify whether it should hug the left or right in its given grid point:

```python
ttk.Button(button_frame, text="Calculate", command=calculate).pack(side="left")
ttk.Button(button_frame, text="Open", command=open).pack(side="left")
ttk.Button(button_frame, text="Anki", command=lambda: presets("44", "44", "44")).pack(side="left")
ttk.Button(button_frame, text="Obsidian", command=lambda: presets("30", "30", "30")).pack(side="left")
```

Lastly the last frame we will create is the grid for the image: `image_label`

```python
image_label = ttk.Label(mainframe)
image_label.grid(column = 1, row = 3, columnspan = 1, pady = 10) # pady is just some padding to make it look nicer
```

This frame is special to the others as it will contain the image and will mean that when we press `Calculate`, we will get the image meaning we should re-size the window accordingly:

```python
mainframe.columnconfigure(0, weight = 1)
mainframe.columnconfigure(4, weight = 1)
mainframe.rowconfigure(4, weight = 1)
```

The above makes the image re-size as we increase/decrease the window dimensions, weight denotes how much it should expand when it grows.

The following code s just for quality of life and to make stuff feel and look a bit nicer, for this one when the user launches the program it will automatically set the focus on the `r_entry` input field as it is the first input of RGB:

```python
r_entry.focus()
```

The following binds the `Enter` key to the `calculate()` function meaning if the user presses the `Enter` key then they will initiate the colour switching.

```python
root.bind("<Return>", calculate)
```

The following changes how the standard `Tkinter` represents its UI to make it look a bit nicer.

```python
style = ttk.Style()
style.theme_use('clam')
  
style.configure('TFrame', background='#1e1e1e')
style.configure('TLabel', background='#1e1e1e', foreground='white')
style.configure('TButton', background='#333333', foreground='white')
```





