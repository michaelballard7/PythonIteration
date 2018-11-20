 


"""
  
 A loop within in a loop is a nested loop

 The inner loop is executed completetly with each new value in the counter variable of outer variable

Any loop can be used as the inner loop for an outer loop
 
""" 


for outer in range(1,6):
    for inner in range(1,6):
        print(outer, inner)