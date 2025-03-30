# Task 1
import traceback

try:
    with open('diary.txt', 'a') as file:
        first_question=input("What happened today?")
        file.write(first_question + "\n")
        
        while True:
            next_question = input("What else? ")
            file.write(next_question + "\n")
            if next_question == "done for now":
                break

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

