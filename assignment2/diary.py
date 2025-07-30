import traceback
try:
    with open('diary.txt', 'w') as file:
        input_user = input("What happened today?")
        content = file.write(f"{input_user}\n")
        flag = True
        try:
            while flag:
                inputCont = input("What else?")
                if inputCont == "Done for now":
                    contentCont = file.write(f"{inputCont}\n")
                    flag = False
                else:
                    contentCont = file.write(f"{inputCont}\n")
               
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

