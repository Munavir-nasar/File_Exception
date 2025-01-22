# question 1

file1 = open("C:\\Users\\MUNAVIR NASIR\\Desktop\\file_handling\\source1.txt",'r')
print(file1.read())

# for i in file1:
#     print(i)

# question 2

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line)
        print("File copied.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except IOError:
        print("An error occurred while copying the file.")
    finally:
        print("The function has completed the task")

source_file = "C:\\Users\\MUNAVIR NASIR\\Desktop\\file_handling\\source1.txt"
destination_file = "C:\\Users\\MUNAVIR NASIR\\Desktop\\file_handling\\destination1.txt"
copy_file("C:\\Users\\MUNAVIR NASIR\\Desktop\\file_handling\\source1.txt",
          "C:\\Users\\MUNAVIR NASIR\\Desktop\\file_handling\\destination1.txt")

# question 3
with open("C:\\Users\\MUNAVIR NASIR\\Desktop\\file_handling\\okay.txt",'r') as file2:
    data = file2.read()
    print(data.split())
    print(len(data.split()))


# question 4
a=input("the string which is to be converted to int: ")
try:
     b=int(a)
     print(b,"the string converted to integer")
except ValueError:
     print("This string cannot be converted to integer")

# question 5
def right_number():
    try:

        user_input = input("Enter a list of integers, separated by spaces: ")

        int_list = [int(num) for num in user_input.split()]


        for num in int_list:
            if num < 0:
                raise ValueError("Negative numbers are not allowed.")

        print("All numbers are non-negative:", int_list)

    except ValueError as e:
        print("Error:", e)

right_number()

# question 6

def finding_average():
    try:
        user_input = input("Enter a list of integers, separated by spaces: ")

        int_list = [int(num) for num in user_input.split()]

        average = sum(int_list) / len(int_list)

        print("The average of integers is:", average)

    except ValueError:
        print("Error: Please enter only integers.")
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of an empty list.")
    finally:
        print("Program has finished running.")
finding_average()

# question 7

def file_writing():
    try:
        filename = input("Enter the filename to write to it: ")

        content = "Good Morning Munavir."

        with open(filename, 'w') as file:
            file.write(content)
            print("Welcome! The text has been successfully written to the file.")

    except Exception as e:

        print("An error occurred:", e)
file_writing()





