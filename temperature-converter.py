from nicegui import ui

# a more professional coloring with darker colors is best
ui.colors(
      primary='#26303b',
      secondary='#789491',
      accent='#613669',
      positive='#5a8f66',
      negative='#cf0018',
      info='#91c49f',
      warning='#dbbf72'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4") 
        # text-lg: This makes the text large (18px)
        # font-semibold: this makes the font semibold
        # text-positive: this makes the text color positive which is stated in our ui colors.
        # mt-4: It adds a top margin on the text of 1rem which is 16px
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4") 
        # text-lg: This makes the text large (18px)
        # font-semibold: this makes the font semibold
        # text-negative: It makes the text color negative from our above ui colors
        # mt-4: It adds a top margin on the text of 1rem which is 16px

def convertSlider(value):
    if conversion2_type.value == "Celsius to Fahrenheit":
        result2_label.set_text(f"{value}°C = {value * 9/5 + 32:.2f}°F")
    else:
        result2_label.set_text(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    result2_label.classes("text-lg font-semibold text-positive mt-4") 



with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl border"): # added a border to make it stand out well in the white background
        # w-100: Set element width to be fixed at 100
        # p-6: Adds padding of 1.5 rem which is around 24 px for all sides of the item
        # shadow-xl: Adds a extra large shadow to the item
        # mx-auto: It centers the item horizontally
        # mt-10: Adds a top margin of 2.5 rem which is about 40px
        # rounded-xl: It rounds the item with extra large radius
        ui.label("Temperature Converter").classes("text-3xl font-bold text-accent mb-4")# made the title bigger to accomodate people. It also helps people understand what this application is about
        # text-2xl: Sets the font to 2 extra large which is around 1.5 rem which is 24 px
        # font-bold: It makes the text bold
        # text-accent: It applies text color accent which is from our above ui colors
        # mb-4: It adds a below margin of 1rem which is 16 px
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: Makes the item take up the full width of its container
        # mb-4: Adds a margin bottom of 1 rem which is 16 px
        # border: Adds a border to the item (probably with the default settings)
        # rounded: It applies rounded corners (of radius 0.25 rem)
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded mx-auto") # I added mx-auto here to center the button. It looks better
        # text-white: It makes the text color white
        # py-2: It adds a top and bottom (vertical) padding of 0.5 rem which is 8px
        # px-4: It adds a left and right (horizontal) padding of 1 rem which is 16 px
        result_label = ui.label("").classes("text-lg mt-4 mx-auto")# added mx-auto here to make the answer centered. It makes it more visually appealing
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl border"):
        ui.label("Slider Temperature Converter").classes("text-3xl font-bold text-accent mb-4")
        slider = ui.slider(min=-150, max=150, value=0, step=1, on_change= (lambda e: convertSlider(e.value))).classes("w-100 mb-5")
        ui.label().bind_text_from(slider, 'value').classes("mx-auto")
        conversion2_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        result2_label = ui.label("").classes("text-lg mt-4 mx-auto")

ui.run()