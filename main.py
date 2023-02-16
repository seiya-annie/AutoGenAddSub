import random
import sys

def generate_addition_subtraction_problems(max_sum, num_problems):
    problems = []
    for i in range(num_problems):
        # 50% 的概率生成加法题目，50% 的概率生成减法题目
        if random.random() < 0.5:
            a = random.randint(0, max_sum)
            b = random.randint(0, max_sum - a)
            problems.append(f"{a} + {b} = ")
        else:
            a = random.randint(0, max_sum)
            b = random.randint(0, a)
            problems.append(f"{a} - {b} = ")
    return problems


if __name__ == '__main__':
    print(sys.argv)
    results = generate_addition_subtraction_problems(int(sys.argv[1]), int(sys.argv[2]))
    for num in results:
        print(num)
