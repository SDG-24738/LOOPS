medical_cause = input("Do you have a medical cause. Y/N")
if medical_cause == "Y":
    print("You're medical cause is accepted. You can write the exam.")
elif medical_cause == "N":
    attendance = int(input("Enter your attendance %?"))
    if attendance >= 75:
        print("You can write the exam")
    else:
        print("You cannot write the exam")

