def main():
    keyWords = {"and", "del", "from", "not", "while",     
                "as", "elif", "global", "or", "with",      
                "assert", "else", "if", "pass", "yield",    
                "break", "except", "import", "print",               
                "class", "exec", "in", "raise",              
                "continue", "finally", "is", "return",              
                "def", "for", "lambda", "try"}

    f1 = input("Enter a Python source code filename: ").strip()

    # Open files for input 
    inputFile = open(f1, "r")
    
    text = inputFile.read().split()
    inputFile.close()
    
    dictionary = {}
    count = 0
    for word in text: 
        if word in keyWords:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    
    print(dictionary)
    
main()
