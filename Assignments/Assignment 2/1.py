
#1: Convert time entered in hh, min and sec into seconds

# Step 1: Take input
hh = int(input('Enter hours: '))
min = int(input('Enter minutes: '))
sec = int(input('Enter seconds: '))

# Step 2: Convert into seconds
total_seconds = (hh * 3600) + (min * 60) + sec

# Step 3: Display result
print("Total seconds are:", total_seconds)