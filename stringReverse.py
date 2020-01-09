#Function to reverse the string given
#Example input:  "gnikrow si ti ih"
#        output: "Hi it is working"

#Steps
# 1. Verify the inputs

def reverse(string):

    if(type(string) != str):
        print("Not a Valid String")
        quit()

    output = ""
    
    for i in range(len(string)-1,-1,-1):
        output=output + string[i]

    return output

def reverse2(string):
    return string[::-1]

print(reverse("gnikrow si ti ih"))
print("".join(reversed("gnikrow si ti ih")))
print(reverse2("gnikrow si ti ih"))
