# Challenge Mode 
 
Members=["Poonam","Gaytri","Disha","Mokshada"] 
Club_Information=("Coding club",2025,"GPH") 
Unique_Skills_of_Members={"Python","HTML","CSS","Python"}

# List Functions 
Members.append("Sanika")
for x in Members:
    print(x) 
Members.remove("Disha")
print(Members) 
Members.insert(3,"Aditi") 
print(Members)
Members.pop() 
print(Members)
Members.sort() 
print(Members)

#Tuple Functions 
print(Club_Information.count("GPH"))
print(Club_Information.index(2025)) 

# Set Functions 
skills={"CSS","HTML","java"}
Unique_Skills_of_Members.add("Python") 
Unique_Skills_of_Members.remove("CSS") 
print(Unique_Skills_of_Members.union(skills))
print(Unique_Skills_of_Members.intersection(skills))