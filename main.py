from colorama import init, Fore, Back, Style
from days.day1 import Day1
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from days.day5 import Day5

# Load console output styles
init(autoreset=True)

# START DAY 1
print(Fore.YELLOW + "========= " + Fore.WHITE + Style.BRIGHT + "BEGIN DAY 1 " + Fore.YELLOW + Style.NORMAL + "=========")
day1 = Day1()
day1.part1()
day1.part2()
print(Fore.YELLOW + "========= " + Fore.WHITE + Style.BRIGHT + "BEGIN DAY 2 " + Fore.YELLOW + Style.NORMAL + "=========")
# END DAY 1

print(Back.BLUE + Fore.BLACK + "########## - NEXT DAY - #######")

# START DAY 2
print("\033[33m========= \033[30mBEGIN DAY 2\033[0m \033[33m=========\033[0m")
day2 = Day2()
day2.part1()
day2.part2()
print("\033[33m========= \033[37mEND DAY 2\033[0m \033[33m===========\033[0m")
# END DAY 2

print(Back.BLUE + Fore.BLACK + "########## - NEXT DAY - #######")

# START DAY 3
print("\033[33m========= \033[30mBEGIN DAY 3\033[0m \033[33m=========\033[0m")
day3 = Day3()
day3.part1()
day3.part2()
print("\033[33m========= \033[37mEND DAY 4\033[0m \033[33m===========\033[0m")
# END DAY 3

print(Back.BLUE + Fore.BLACK + "########## - NEXT DAY - #######")

# START DAY 4
print("\033[33m========= \033[30mBEGIN DAY 4\033[0m \033[33m=========\033[0m")
day4 = Day4()
day4.part1()
day4.part2()
print("\033[33m========= \033[37mEND DAY 4\033[0m \033[33m===========\033[0m")
# END DAY 4

print(Back.BLUE + Fore.BLACK + "########## - NEXT DAY - #######")

# START DAY 5
print("\033[33m========= \033[30mBEGIN DAY 5\033[0m \033[33m=========\033[0m")
day5 = Day5()
day5.part1()
day5.part2()
print("\033[33m========= \033[37mEND DAY 5\033[0m \033[33m===========\033[0m")
# END DAY 4
