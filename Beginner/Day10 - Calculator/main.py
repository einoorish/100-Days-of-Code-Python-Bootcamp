import art


def calculate(first_number, second_number, operation) : 
  result = 0

  if(operation == "+"):
    result = first_number+second_number
    return result
  elif(operation == "-"):
    result = first_number-second_number
    return result  
  elif(operation == "*"):
    result=first_number*second_number
    return result
  elif(operation == "/"):
    result=first_number/second_number
    return result
  else :
    return "Wrong input."

def start_new_calculation() :  
  '''
  This is a docstring example.
  They're used to create documentation for your functions
  '''
  print(art.logo)
  first_number = input("What's the first number: ")
  continue_calculation_with(first_number)

def continue_calculation_with(first_number) :

  print("+\n-\n*\n/\n")
  operation = input("Pick an operation from the line above: ")
  second_number = input("What's the second number? ")

  calculation_result = calculate(float(first_number), float(second_number), operation)

  result_text = f"{first_number} {operation} {second_number} = {calculation_result}\n"

  print(result_text)

  reset_or_continue(calculation_result)


def reset_or_continue(prev_result):
  should_continue = input(f"Type 'yes' to continue calculating with {prev_result} or type 'no' to start a new calculation\n")
  if should_continue == "yes":
    continue_calculation_with(prev_result)
  else : start_new_calculation()

start_new_calculation()

