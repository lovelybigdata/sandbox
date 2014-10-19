count=0
total=0
average=0

while True:
    x=raw_input("Please enter a number:  ")

    try :
        y=int(x)
        
    except :
        if x=="done" :
            print total , count , average
            break
        else:
            print "invalid input , try again"

    total=total+y
    count=count+1
    average=total/count
     