
# Create a variable called `text` to store the data: `Berlin is surrounded by the State 
# of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . 

# Your task is to replace the word `capital` with the phrase  `capital of Germany` .

# - Your result should look like this:

# ```
# Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, 
# Brandenburg's capital of Germany.
# ```
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

new_text = text.replace("capital", "capital of Germany")
print(new_text)
