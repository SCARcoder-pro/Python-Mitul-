set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'D', 'E', 'F', 'G', 'H'}

union = set1.union(set2)
total_guests = list(union) 
print("Total guests to be invited to party are: ", len(total_guests))
print("Guests list: ", total_guests)