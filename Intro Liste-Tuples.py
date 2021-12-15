#%%
#First List
Langs = ["python", "c", "java"];

lang =Langs[0];
print(lang.title());
lang=Langs[1];
print(lang.title());
lang=Langs[2];
print(lang.title());

#%%
#First Neat List
Langs = ["python", "c", "java"];

print("A nice programming language is " + Langs[0].title());
print("A nice programming language is " + Langs[1].title());
print("A nice programming language is " + Langs[2].title());

#%%
#Your First list
shop_list = ["lessive vaisselle","lessive linge", "shampooing", "café", "petit dèj"];

print("One item in my shopping list is : " + shop_list[2]);

#%%
#First List - Loop
Langs = ["python", "c", "java"];

for lang in Langs:
    print(lang.title());    
#%%
#First Neat List - Loop
Langs = ["python", "c", "java"];

for lang in Langs:
    print("A nice programming language is " + lang.title() + "."); 

#%%
#Your First List - Loop
shop_list = ["lessive vaisselle","lessive linge", "shampooing", "café", "petit dèj"];

for shop_item in shop_list :
    print("In my shopping list I have : " + shop_item);

#%%
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

#%%
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

#%%
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

#%%
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

#%%
#List Lengths
Careers_count = len(Careers);
Langs_count = len(Langs);

print("My Career list as %s different jobs in it and my programming language list as %s different languages in it." %(str(Careers_count), str(Langs_count)))

#%%
#Alphabet Slices
Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
First_alpha = Alpha[:3]
Middle_alpha = Alpha[3:6]
End_alpha = Alpha[7:]

for letter1 in First_alpha:
    print(letter1);
print("\n");
for letter2 in Middle_alpha:
    print(letter2);
print("\n");
for letter3 in End_alpha:
    print(letter3);

#%%
#Protected List
Names = ["Arthur", "Vincent", "Martin"]
Names_copie = Names[:3];

Names.insert(2, "Ulysse");
Names.append("Joseph");

print("This is the original list :");
for name1 in Names:
    print(name1);
print("\n");
print("This is the copie made from a slice")
for name2 in Names_copie:
    print(name2);

#%%
#First Twenty
for Numbers in range(1,21):
    print(Numbers);

#%%
#Larger Sets
for Numbers2 in range(1, 1000001):
    print(Numbers2);

#%%
#Five Wallets
Wallets = [654, 89710, 367180, 16485, 24768]
Max_Wallet = max(Wallets);
Min_Wallet = min(Wallets);
Sum_Wallet = sum(Wallets);

print("The fattest wallet has " + str(Max_Wallet) + " in it.");
print("The skinniest wallet has %s in it" %Min_Wallet);
print("All together, these wallets have %d in it" %Sum_Wallet);

#%%
#Multiple of Ten

Multi = [number*10 for number in range(1,11)];

for numb in Multi:
    print(numb);

#%%
#Cubes
Cubes = [cube**3 for cube in range(1,11)];

for cube in Cubes:
    print(cube);
    
#%%
#Awesomeness
