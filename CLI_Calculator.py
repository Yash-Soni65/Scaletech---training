while True:
 try:

  a,b = float(input('Enter first number: ')), float(input('Enter second number: '))
  input_operator = input('Enter operator (+, -, *, /): ')
  if input_operator == '+':
   res = a + b
  elif input_operator == '-':
    res = a - b
  elif input_operator == '*':
    res = a * b
  elif input_operator == '/':
    res = a / b
  else:
    raise ValueError('Invalid operator')
    

  print("your result of operation ",a,input_operator,b, "is =", res)

 except ValueError as e:
   print("error: ", e) 
 except ZeroDivisionError :
   print("error: division by zero is not allowed")
   break  



 
