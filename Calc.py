num1 = input("ჩაწერეთ პირველი რიცხცი: ")
num2 = input("ჩაწერეთ  მეორე  რიცხვი: ")
operation = input("ჩაწერეთ ერთი ოპერაცია შემდეგი სიიდან:\n1)მიმატება +\n2)გამოკლება -\n3)გამრავლება *\n4)გაყოფა /\n")
legal_operations = ["+", "-", "*", "/"]
if num1.replace('.', '', 1).lstrip('-').isdigit() and num2.replace('.', '', 1).lstrip('-').isdigit() and operation in legal_operations:
    if operation == "/" and float(num2) == 0:
        print("ნულზე გაყოფა არ შეიძლება")
    else:
        print(eval(num1+operation+num2))
else:
    print("გთხოვთ მიყვეთ ინსტრუქციას. ჩაწეროთ მხოლოდ რიცხვები გამოტოვების გარეშე და ოპერაციები მითითებული სიიდან")
