'''
有一个很奇怪的问题，python的批量注释，会导致 while... else... 中的 else 报 invalid syntax 错误，不知原因，有高手见到还请赐教
'''

# source code1:
# ---------------------------------------------------------------

import random

num_random = random.randint(1,101)
count = 0

while count < 10:

    num_input = int(input("请输入您的整数数字（1~100）："))
    
    count += 1

    if num_input == num_random:
        print("恭喜您，猜对了。。。,共猜了 %d 次"%count)
        break

    elif num_input > num_random:
        print("您输入的数字太大，再输入个小一点的数试试。。")       

    else:
        print("您输入的数字太小，大一些。。")

# 使用"#"注释，执行时，下面41行的 else 语句不会报错。
#    if count == 10:
#        
#        game_again = input("您已猜了10次，仍然没有猜中，是否继续游戏(yes/no)?")
#
#        if game_again == "yes":
#            count = 0
#
#        else:
#            break

else:
    print("猜了10次都没有猜中，太遗憾了。。")
# ---------------------------------------------------------------




# source code2:
# ---------------------------------------------------------------
import random


num_random = random.randint(1,101)
count = 0

while count < 10:

    num_input = int(input("请输入您的整数数字（1~100）："))
    
    count += 1

    if num_input == num_random:
        print("恭喜您，猜对了。。。,共猜了 %d 次"%count)
        break

    elif num_input > num_random:
        print("您输入的数字太大，再输入个小一点的数试试。。")       

    else:
        print("您输入的数字太小，大一些。。")

# 使用单引号或者双引号批量注释时，执行时，下面83行的 else 就会报invalid syntax 错误。
'''       
    if count == 10:
        
        game_again = input("您已猜了10次，仍然没有猜中，是否继续游戏(yes/no)?")

        if game_again == "yes":
            count = 0

        else:
            break
'''

else:
    print("猜了10次都没有猜中，太遗憾了。。")
# ---------------------------------------------------------------




# source code3:
# ---------------------------------------------------------------
import random


num_random = random.randint(1,101)
count = 0

while count < 10:

    num_input = int(input("请输入您的整数数字（1~100）："))
    
    count += 1

    if num_input == num_random:
        print("恭喜您，猜对了。。。,共猜了 %d 次"%count)
        break

    elif num_input > num_random:
        print("您输入的数字太大，再输入个小一点的数试试。。")       

    else:
        print("您输入的数字太小，大一些。。")

else:
    print("猜了10次都没有猜中，太遗憾了。。")
    
# 和source code2一样的代码，使用单引号或者双引号批量注释时，把注释掉的代码放到 else 的后面，再执行时，就不会报错。
'''       
    if count == 10:
        
        game_again = input("您已猜了10次，仍然没有猜中，是否继续游戏(yes/no)?")

        if game_again == "yes":
            count = 0

        else:
            break
'''
# ---------------------------------------------------------------
