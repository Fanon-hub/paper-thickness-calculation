# define the initial thickness of the paper
Thickness = 0.00008 # Thickness in metres
# creating an empty list to store the thickness values
thickness_list =[]

# add the initial thickness to the list
thickness_list.append(Thickness)
# use a for loop to calculate the thickness for each fold and store it in the list 
folded_thickness=Thickness
for _ in range(43):
    folded_thickness = folded_thickness *2 #Double the thickness of each fold
    thickness_list.append(folded_thickness)
# check that the 44 values are stored in the list 
print("Number of thickness values:", len(thickness_list))


print("Thickness values:", thickness_list)

import matplotlib.pyplot as plt
# plot the thickness values
plt.plot(thickness_list, 
         color='yellow',
         linestyle=':',
         linewidth='2.5',
         marker='*',
         markerfacecolor='green',
         markeredgecolor='black')

plt.title("Paper Thickness Growth After Each Fold")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness (meters)")

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.grid(True)
plt.show()
