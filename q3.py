# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE 
with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()
####

# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 

newtext = text.split(" ")
julietcounter = 0
for word in newtext:
    if "Juliet" in word:
        julietcounter = julietcounter + 1
print(julietcounter)

####
