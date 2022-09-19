from os import system

# run a command on the system
def run(cmd):
    print("Running:",cmd)
    if (system(cmd) != 0):
        raise RuntimeError("Command failed")

run("clang++ -Wall -Wextra -pedantic -c -std=c++17 cow.cpp")
run("clang++ -Wall -Wextra -pedantic -c -std=c++17 main.cpp")
run("clang++ -std=c++17 -o main main.o cow.o")

print("All done.")