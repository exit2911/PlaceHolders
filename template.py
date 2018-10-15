from string import Template


def main():

    str1 = "you're watching {0} by {1}".format("nothing","nothing")    
    print(str1)
    
    templ = Template("you're watching ${title} by ${author}")
    
    str2 = templ.substitute(title = "nothing", author ="nothing")
    print(str1)
    
        
    data = {
        
        "author":"no one","title":"nothing"
        
        } #set a dictionary

    str3 = templ.substitute(data) #substitute data from the dictionary using keys
    print(str3)
    
if __name__ == "__main__":
    
    main()
    
    
    
