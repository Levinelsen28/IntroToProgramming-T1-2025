def classifier_hurricane(windspeed):
    if windspeed < 74:
        print("tropical storm")
    elif windspeed < 96:
        print("Category 1")
    elif windspeed < 111:
        print("Category 2")
    elif windspeed < 130:
        print("Cateogory 3")
    elif windspeed < 157:
        print("Category 4")
    else:
        windspeed >= 157 
        print("Category 5")
        
    return

classifier_hurricane(160)