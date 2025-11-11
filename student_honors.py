# Author: Mohamad Suhail Mohamad Solim
# File Name: student_honors.py
# Description: This application accepts student names and GPAs to determine
#              if they qualify for the Dean's List (GPA >= 3.5)
#              or the Honor Roll (GPA >= 3.25).

def get_gpa():
    """
    Prompts the user to enter a GPA and validates the input.
    Ensures the input is a valid float between 0.0 and 5.0 (or a reasonable range).
    """
    while True:
        try:
            gpa = float(input("Enter student's GPA: "))
            
            if 0.0 <= gpa <= 5.0:
                return gpa
            else:
                print("Invalid GPA. Please enter a value between 0.0 and 5.0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the GPA.")

def main():
    """
    Main function to run the student honors program.
    """
    print("Student Honors Qualification App")
    print("================================")
    print("Enter 'ZZZ' for the last name to quit.")
    
    while True:
        last_name = input("\nEnter student's last name (or 'ZZZ' to quit): ")
        
        if last_name.upper() == 'ZZZ':
            break
            
        first_name = input("Enter student's first name: ")
        
        gpa = get_gpa()
        
        full_name = f"{first_name} {last_name}"
        
        honor_awarded = False
        
        if gpa >= 3.5:
            print(f"\n*** Congratulations, {full_name}! You have made the Dean's List. ***")
            honor_awarded = True
        elif gpa >= 3.25:
            print(f"\n*** Congratulations, {full_name}! You have made the Honor Roll. ***")
            honor_awarded = True
        
        if not honor_awarded:
            print(f"\n{full_name} does not qualify for an honor roll at this time.")
            
        print("-" * 30)

    print("\nThank you for using the Student Honors App. Goodbye!")

if __name__ == "__main__":
    main()