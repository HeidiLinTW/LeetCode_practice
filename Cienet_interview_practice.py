def fib_heidi(n: int):
    num_list = [0, 0, 1]
    if 0 > n:
        return 'invalid input'
    elif n <= 2:
        print(num_list)
        return num_list[n]
    else:
        while len(num_list) <= n:
            num_list.append(num_list[-1] + num_list[-2])

        print(num_list)

    return num_list[n]


def fib_recursive(n: int):
    if n < 0:
        return 'invalid input'
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


if __name__ == "__main__":
    # #3
    # i = 0
    #
    # def foo(arg=[]):
    # 	global i
    # 	arg.append(i)
    # 	i += 1
    #
    # 	return arg
    #
    # print(foo([]))
    # print(foo([]))
    # print(foo())
    # print(foo())

    # # 6 Fibonacci function
    # test_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # ans = [0, 0, 1, 1, 2, 3, 5, 8, 13]
    # for i in range(len(test_data)):
    #     ans_from_function = fib_recursive(test_data[i])
    #     if ans_from_function == ans[i]:
    #         print(f'test data:{test_data[i]}/ans:{ans[i]}/result: Pass')
    #     else:
    #         print(
    #             f'test data:{test_data[i]}/func:{ans_from_function}/ans:{ans[i]}')


    def process(target, proc):
        for i in target:
            result = proc(i)
        return result

    def sum(s):
        process(s, gen_proc)


    def gen_proc(num):
        # complete this function
        num = int(num)

    # for i in "123":
    #     print(i)
    #     print(type(i))




