#Hello World - variable
Hello = "Hello World";
print(Hello);

print("\n");
#One Variable, Two Messages
message = "Bonjour";
print(message);

message = "Je m'appelle Arthur.";
print(message);

print("\n");
#Someone Said
quote = "When a game is going full retard, you can only go with it. If you start going against it, if you start going half retard you're fucking done for.";
print("Johan 'N0tail' Sundstein once said : " + quote);

print("\n");
#First Name Cases
name = "arthur";
print(name);
print(name.title());
print(name.upper());

print("\n");
#Full Name
first_name = "Arthur"
last_name = "Allain"
full_name = first_name + " " + last_name;
print(first_name + " " + last_name);
print(full_name);

print("\n");
#About this Person
First_name = "Albert";
Last_name = "Falco";
print(First_name + " " + Last_name + " was a french diver working for Jacques-Yves Cousteau.\n He spent more than 20 000 hours under the ocean around the globe.\n I was lucky enought to meet him twice.");

print("\n");
#Name Stripe
Name = "\tArthur\n";
print(Name);
print(Name.lstrip());
print(Name.rstrip());
print(Name.strip());

print("\n");
#Arithmetic
num1 = 7;
num2 = 9;
print(num1 + num2);
print(num1 - num2);
print(num1 * num2);
print(num1 / num2);
print(num1 ** num2);

print("\n");
#Order of Operation
num3 = 8;
num4 = 2;
num5 = 5;
print(num3 + num4 * num5);
print((num3 + num4)* num5);

print("\n");
#Long Decimals
dec1 = 2.5
dec2 = 1.6
print(dec1 - dec2);

print("\n");
#Python 2 or Python 3?
print (4/2);
print (3/2);

print("\n");
#Neat Arithmetic 
add = num1 + num2;
sub = num1 - num2;
mult = num1 * num2;
div = num1 / num2;
expo = num1 ** num2;
print("The result of the calculation %d + %d is %d." %(num1, num2, add));
print("The result of the calculation %d - %d is %d." %(num1, num2, sub));
print("The result of the calculation %d * %d is %d." %(num1, num2, mult));
print("The result of the calculation %d / %d is %d." %(num1, num2, div));
print("The result of the calculation %d ** %d is %d." %(num1, num2, expo));

print("\n");
#Neat Order of Operations
res1 = num3 + num4 * num5;
res2 = (num3 + num4)* num5;
print("The multiplication takes precedent over the addition so %d + %d * %d = %d" %(num3, num4, num5, res1));
print("if you put paranthesis around an operation then the content inside those parenthesis takes priority above any other operation so (%d + %d) * %d = %d" %(num3, num4, num5,res2))

print("\n");
#Long Decimals - Pattern
