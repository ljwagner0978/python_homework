import traceback

if __name__ == "__main__":
    try: 
        with open('diary.txt', 'w') as file:
            line = input("What happened today? ")
            while line != "done for now":
                file.write(f"{line}\n")
                line = input("What else? ")
            file.write(f"{line}")
        with open("../assignment2/diary.txt", 'r') as file:
            print("Diary entry complete, written as .txt file successfully.")
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
    