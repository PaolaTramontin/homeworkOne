def occurances(strings, letter):
    times = 0
    for i in strings:
        if  i == letter:
            times = times+1
    print("this is how many times", times)    
        
    
    
    
    
occurances('fleep floop', 'e') 