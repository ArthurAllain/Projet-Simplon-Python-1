#First List
langs = ["python", "c", "java"];

lang =langs[0];
print(lang.title());
lang=langs[1];
print(lang.title());
lang=langs[2];
print(lang.title());

print("\n")
#First Neat List
langs = ["python", "c", "java"];

print("A nice programming language is " + langs[0].title());
print("A nice programming language is " + langs[1].title());
print("A nice programming language is " + langs[2].title());

print("\n")
#Your First list
shop_list = ["lessive vaisselle","lessive linge", "shampooing", "café", "petit dèj"];

print("One item in my shopping list is : " + shop_list[2]);

print("\n")
#First List - Loop
langs = ["python", "c", "java"];

for lang in langs:
    print(lang.title());
    
print("\n")
#First Neat List - Loop
langs = ["python", "c", "java"];

for lang in langs:
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
Careers


# print("\n");
# #Ordered Numbers
# Nums = [1, 8, 6, 7, 3];
# Nums_sort = sorted(Nums);

# for Num1 in Nums:
#     print(Num1)
    
# print("\n");

# for Num2 in Nums_sort:
#     print(Num2);

# print("\n");    

# for Num1 in Nums:
#     print(Num1)
    
# print("\n");


