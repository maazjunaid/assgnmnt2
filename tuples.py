temp_days1 = {'Monday' : 25,  'Tuesday' : 30 , 'wednesday' : 26 , 'Thursday' : 27
    , 'friday' : 28 , 'Saturday' : 33 , 'Sunday' : 29 }

print("Days along with its temperature : " ,temp_days1)

print("Maximum temperature along with its day : " ,max(temp_days1.values()) ,  max(temp_days1 , key=temp_days1.get))

average = sum(temp_days1.values())
print("Sum of temperature is : ",average)
length = len(temp_days1)
print("length of temperature is " ,length)

print("Average Temperature is : " , average/length)