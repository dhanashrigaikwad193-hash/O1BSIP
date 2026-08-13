print("===== BMI CALCULATOR =====")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive.")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("\nYour BMI is:", round(bmi, 2))
        print("Category:", category)

        again = input("\nCalculate again? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using BMI Calculator!")
            break

    except ValueError:
        print("Please enter valid numbers.")