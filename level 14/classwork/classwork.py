# Level 14
# 1) მომხმარებელს შემოატანინეთ თავისი სახელი, შეამოწმეთ თუ ის უდრის "davit"-ს, მაშინ დაბეჭდეთ "გაუმარჯოს დავით". სხვა შემთხვევაში "შენ არ ხარ დავითი"

# 2) მომხმარებელს შემოატანინეთ ამინდი და თუ ის არის "მზიანი", დაბეჭდეთ "ვივარჯიშებ გარეთ", სხვა შემთხვევაში თუ "მოღრუბლულია"-ა მაშინ დაბეჭდეთ "ვივარჯიშებ გარეთ ოღონდ მოგვიანებით", ხოლო სხვა დანარჩენ შემთხვევაში დაბეჭდეთ "საერთოდარ ვივარჯიშებ დღეს"

#1
name = input("enter your name: ")
if name == "davit":
    print("gaumarjos davit")
else:
    print("shen ar xar daviti")

#2
weather = input("enter weather: ")
if weather == "mziani":
    print("vivarjisheb garet")
elif weather == "mogrublulia":
    print("vivarjisheb garet oghond mogvianebit")
else:
    print("saertod ar vivarjisheb dges")