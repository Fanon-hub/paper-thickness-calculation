# define the initial thickness of the paper
Thickness = 0.00008 # Thickness in metres
# calculating the thickness of the paper after folding 43 times
folded_thickness = Thickness*(2**43)

#print the result
print("Thickness:{} metres".format(folded_thickness))