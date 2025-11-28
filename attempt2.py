#read the README.md file in order to know how to use this thing. i forgot about it and had to learn from looking at how it parsed operations 
import os
if not os.path.exists("ProgramFiles"):
    os.system("mkdir ProgramFiles")
while True:
    #find the first .pyasm file
    pyasm_file = None
    os.chdir("ProgramFiles")
    for file in os.listdir():
        if file.endswith(".pyasm"):
            pyasm_file = file
            break

    if not pyasm_file:
        print("No .pyasm file found.")
        break  # exit if none found

    print(f"\nReading instructions from {pyasm_file}...\n")
    print("fyi you can NOT do non binary arithmetic but output will be binary. its also a integer only system. look at the source code i tried\n")

    #read and process each line
    with open(pyasm_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # skip empty lines or comments

            try:
                operation, a_str, b_str = [x.strip() for x in line.split(",")]
                a = int(a_str)
                b = int(b_str)
            except ValueError:
                print(f"Invalid line format: {line}")
                continue

            # 3️⃣ Perform the operation
            op = operation.lower()
            if op == "add":
                result = a + b
            elif op == "sub":
                result = a - b
            elif op == "mult":
                result = a * b
            elif op == "div":
                result = float(a) / float(b)
                if b == 0:
                    print("DIVISION BY 0")
                    exit	
                elif a == 0:
                    print("DIVISION BY 0")
                    exit    
            elif op == "xor":
                if a == 1 and b == 1:
                    result = 0
                elif a == 1 and b == 0:
                    result = 1
                elif a == 0 and b == 1:
                    result = 1
                elif a == 0 and b == 0:
                    result = 0            
            else:
                print(f"Illegal instruction: {operation}")
                continue

            # 4️⃣ Print binary result (without '0b')
            print(f"{operation.upper()} {a} {b} -> {bin(result)[2:]}") #even after trying all this it still wont do floats. i undid my changes i fucking hate this bullshit
#why isnt there a magic function to fix this bullshit like make_float(a,b). oh wait, float(a) float(b) too damn bad i forgot about this language entirely while learning C and i dont understand any of this code.
    # 5️⃣ Wait before looping again
    input("\nPress Enter to re-run or Ctrl+C to exit...")
    import sys

    # after every 100 prints or so:
    sys.stdout.flush()
