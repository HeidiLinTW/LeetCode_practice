"""
Moxa
1. reverse string
ex: input ['a', 'b', 'c', 'd'].  output ['d', 'c', 'b', 'a']
2. move zero to the end of list
ex: input [0, 1, 0, 0, 2, 3].  output [1, 2, 3, 0, 0, 0]
3. determine if an integer is power of 3
ex: input 27.  output True, input 8 output False
4. input “1.2.3.4” output “1[.]2[.]3.[.]4”
"""
import decimal
import math


def reverse_string(input_data: list):
    list_len = len(input_data)
    output = []
    for i in range(list_len):
        output.append(input_data[list_len - 1 - i])

    return output


def move_zero_to_the_end(input_data: list[int]):
    list_len = len(input_data)
    output = []
    for number in input_data:
        if number > 0:
            output.append(number)

    x = list_len - len(output)

    if x == 0:
        return output
    else:
        zero_list = [0 for i in range(x)]
        return output + zero_list


def power_of_three(input_data: int):
    if input_data == 1:
        return True
    elif input_data <= 0:
        return False
    else:
        # while input_data % 3 == 0 and input_data >= 3:
        while input_data % 3 == 0:
            input_data = input_data // 3

        return input_data == 1


def isPowerOfThree(input_num: int) -> bool:
    """
    :type input_num: int
    :rtype: bool
    """
    # Since error exist, can't use float.is_integer() to check
    # So I choose to check it back
    if input_num <= 0: return False
    res = round(math.log(input_num, 3))
    print(res)
    return 3 ** res == input_num


def change_input(input_data: str):
    """
    input “1.2.3.4” output “1[.]2[.]3.[.]4”
    """
    content = input_data.split('.')
    return '[.]'.join(content)


if __name__ == "__main__":
    # answer_reverse_string = reverse_string(['a', 'b', 'c', 'd'])
    # assert answer_reverse_string == ['d', 'c', 'b', 'a'], answer_reverse_string
    #
    # answer_move_zero_to_the_end = move_zero_to_the_end([0, 1, 0, 2, 0, 2, 3, 7, 7, 8])
    # assert answer_move_zero_to_the_end == [1, 2, 2, 3, 7, 7, 8, 0, 0, 0], answer_move_zero_to_the_end

    # test_data_power_of_three = [0, -1, -3, 1, 3, 6, 8, 27, 81]
    # answer_power_of_three_test = [False, False, False, True, True, False, False, True, True]
    # test_data_len = len(test_data_power_of_three)
    # for i in range(test_data_len):
    #     # answer_power_of_three_func = power_of_three(test_data_power_of_three[i])
    #     answer_power_of_three_func = isPowerOfThree(test_data_power_of_three[i])
    #     if answer_power_of_three_func != answer_power_of_three_test[i]:
    #         print(f'test data:{test_data_power_of_three[i]}/func:{answer_power_of_three_func}/ans:{answer_power_of_three_test[i]}')
    #     else:
    #         print(f'test data:{test_data_power_of_three[i]}/ans:{answer_power_of_three_test[i]}/result: Pass')

    test_data_change_input = '1.2.3.4'
    answer_change_input = change_input(test_data_change_input)
    if answer_change_input != '1[.]2[.]3[.]4':
        print(f'test_data:{test_data_change_input}/func:{answer_change_input}/ans:{"1[.]2[.]3[.]4"}')
    else:
        print(f'test data:{test_data_change_input}/ans:{answer_change_input}/result: Pass')

