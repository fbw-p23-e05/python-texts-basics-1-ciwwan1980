# Create a variable called `text` to store the data: `Berlin straddles the banks of the Spree, 
# which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.` 
# . Your task is to split the content of the `text` variable and store it in a list.

# - Your result should look like this:

# ```
# ['Berlin', 'straddles', 'the', 'banks', 'of', 'the', 'Spree,', 'which', 'flows', 'into', 'the', 'Havel', '(a', 'tributary', 'of', 'the', 'Elbe)', 'in', 'the', 'western', 'borough', 'of', 'Spandau.']
# ```


text="Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

#print(text.split(" "))

result_list = text.split(" ")
print(result_list)