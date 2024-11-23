# define the initial thickness of the paper
Thickness = 0.00008 # Thickness in metres
# calculating the thickness of the paper after folding 43 times
folded_thickness = Thickness
# use a for loop to simulate folding thr paper for 43 times
for _ in range(43):
    folded_thickness = folded_thickness *2 #Double the thickness of each fold

print("Thickness: {} meters".format(folded_thickness))

