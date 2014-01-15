my_name = "Alexandra"
friend1 = "Caroline"
friend2 = "Jimbo"

my_age = 22
friend1_age = 21
friend2_age = 23

total_years = my_age + friend1_age + friend2_age
subtraction = friend2_age - my_age
multiplication = friend1_age * friend2_age
division = my_age / friend1_age


print "My name is", my_name, "and I have two friends."
print "My friends are named %s and %s." % (friend1, friend2)
print "I am", my_age, ",", friend1, "is", friend1_age, "and", friend2, "is", friend2_age, "."
print "Combined, we have %d years of experience on this earth." % total_years
print "This is going to be a bad story, I'm sorry."
print "%s is %d year(s) older than me." % (friend2, subtraction)
print "If you multiply", friend1, "'s age by", friend2, "'s age you get", multiplication, "."
print "If you divide %s's age by my age, you get %d." % (friend1, division)