#First List
Langs = ["python", "c", "java"];

lang =Langs[0];
print(lang.title());
lang=Langs[1];
print(lang.title());
lang=Langs[2];
print(lang.title());
print("\n")

#First Neat List
Langs = ["python", "c", "java"];

print("A nice programming language is " + Langs[0].title());
print("A nice programming language is " + Langs[1].title());
print("A nice programming language is " + Langs[2].title());
print("\n")

#Your First list
shop_list = ["lessive vaisselle","lessive linge", "shampooing", "café", "petit dèj"];

print("One item in my shopping list is : " + shop_list[2]);
print("\n")

#First List - Loop
Langs = ["python", "c", "java"];

for lang in Langs:
    print(lang.title());    
print("\n")

#First Neat List - Loop
Langs = ["python", "c", "java"];

for lang in Langs:
    print("A nice programming language is " + lang.title() + ".");    
print("\n")

#Your First List - Loop
shop_list = ["lessive vaisselle","lessive linge", "shampooing", "café", "petit dèj"];

for shop_item in shop_list :
    print("In my shopping list I have : " + shop_item);
print("\n")

#Working List
Careers = ["Streamer", "Progammer", "Truck driver", "Teacher", "Engineer"];
index = Careers.index("Teacher");

print(index);

print("Teacher" in Careers);

Careers.append("Mason");
print(Careers);

Careers.insert(0, "Marine Biologist");
print(Careers);

for index in Careers:
    print(index);
print("\n")

#Starting From Empty
Careers = []
print(Careers);

Careers.append("Marine Biologist");
print(Careers);

Careers.append("Streamer");
print(Careers);

Careers.append("Programmer");
print(Careers);

Careers.append("Truck driver");
print(Careers);

Careers.append("Teacher");
print(Careers);

Careers.append("Engineer");
print(Careers);

Careers.append("Mason");
print(Careers);

print("My first career choice was : " + Careers[0] + " and my last career choice was : " + Careers[3] + "." )
print("\n");

#Ordered Working List
Careers = ["Streamer", "Progammer", "Truck driver", "Teacher", "Engineer"];
Careers_sort = sorted(Careers);
Careers_rev_sort = sorted(Careers, reverse=True);
Careers_rev = reversed(Careers);

print("Liste dans l'ordre original :");
for index1 in Careers:
    print (index1);
print("\n");

print("Liste dans l'ordre alphabétique :")
for index2 in Careers_sort:
    print(index2);
print("\n");    

print("Liste dans l'ordre original :");
for index1 in Careers:
    print (index1);
print("\n");

print("Liste dans l'ordre alphabétique inversé")
for index3 in Careers_rev_sort:
    print(index3);
print("\n");

print("Liste dans l'ordre original :");
for index1 in Careers:
    print (index1);
print("\n");

print("Liste inversée :");
for index4 in Careers_rev:
    print(index4);
print("\n");

print("Liste dans l'ordre original :");
for index1 in Careers:
    print (index1);
print("\n");

print("Liste dans l'ordre alphabétique de façon permanante")
Careers.sort();
for index5 in Careers:
    print(index5);
print("\n");

print("Liste dans l'ordre alphabétique inversé de façon permanante")
Careers.sort(reverse=True);
for index6 in Careers:
    print(index6);
print("\n");

#Ordered Numbers
Nums = [1, 8, 6, 7, 3];
Nums_inc = sorted(Nums);
Nums_dec = sorted(Nums, reverse=True);
Nums_rev = reversed(Nums);

print("Print the numbers in the original order :");
for Num1 in Nums:
    print(Num1)
print("\n");

print("Print the numbers in increasing order :");
for Num2 in Nums_inc:
    print(Num2);
print("\n");    

print("Print the numbers in the original order :");
for Num1 in Nums:
    print(Num1)
print("\n");

print("Print the numbers in decreasing order :");
for Num3 in Nums_dec:
    print(Num3);
print("\n");

print("Print the numbers in the original order :");
for Num1 in Nums:
    print(Num1)
print("\n");

print("Print the numbers in the reverse order from how they started :")
for Num4 in Nums_rev:
    print(Num4);
print("\n");

print("Print the numbers in the original order :");
for Num1 in Nums:
    print(Num1)
print("\n");

print("Permanently sort the numbers in increasing order, and then print them out :")
Nums.sort();
for Num5 in Nums:
    print(Num5);
print("\n");

print("Permanently sort the numbers in descreasing order, and then print them out.")
Nums.sort(reverse=True);
for Num6 in Nums:
    print(Num6);
print("\n");

#List Lengths
Careers_count = len(Careers);
Langs_count = len(Langs);

print("My Career list as %s different jobs in it and my programming language list as %s different languages in it." %(str(Careers_count), str(Langs_count)))
print("\n");

#Alphabet Slices
Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
First_alpha = Alpha[:3]
Middle_alpha = Alpha[3:6]
End_alpha = __uii

