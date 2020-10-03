

def bmi(w,h):
    bmi = w/pow(h,2)
    return bmi

def recommend(bmi):
    rec = ""
    if bmi < 18.5 :
        rec= "thin"
    elif bmi <22.9:
        rec= "normal"
    elif bmi<24.9:
        rec= "fat 1"
    elif bmi<29.9:
        rec= "fat 2"
    else:
        rec= "fat 3"
    return rec

weight = input("Enter your weight: ")
weight = float(weight)
print(weight)

height = input("Enter your height: ")
height = float(height)
print(height)

bmi = bmi(weight,height)
print("bmi = {:.2f}".format(bmi))
print(recommend(bmi))