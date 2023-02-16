import random

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

    results = generate_addition_subtraction_problems(100, 10)
    for num in results:
        print(num)
