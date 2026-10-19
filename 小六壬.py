##小六壬

##dictionary
sequence_dict = {
     "大安": "（吉）身安、事安，大吉大利，凡事容易成功。",
     "留连": "（凶）运气平平，凡事拖延、纠缠不清、官司或行程受阻。",
     "速喜": "（吉）喜事就在眼前，人快到、信速至，诸事顺利。",
     "赤口": "（凶）易有口舌争执、官非、纠纷、血光或不顺。",
     "小吉": "（吉）行事遇贵人，小有成就，结果平和良好。",
     "空亡": "（凶）最凶之兆，音信全无、落空、失财或徒劳无功。"}

keys_list = list(sequence_dict.keys()) ##dont understand its significance

def get_dynamic_key(user_input, start_key):
    """
    Calculates the next Xiao Liu Ren element starting from `start_key` based on input and starting position
    """
    step = int(user_input) - 1 
    start_index = keys_list.index(start_key) ##dont understand its significance
    final_index = (start_index + step) % len(keys_list)
    return keys_list[final_index]

def valid_input(numbers):
    while True:
        try:
            user_input = int(input(numbers))
            if 1 <= user_input <= 99:
                return user_input
            print("请输入数字（1-99）。")
        except ValueError:
            print("请输入号码（1-99）。")

## User Interface
print("=== 小六壬 ===")
user_question = input("问题： ")

user_input_1 = valid_input("数字1（1-99）: ")
user_input_2 = valid_input("数字2（1-99）: ")
user_input_3 = valid_input("数字3（1-99）: ")

# Chaining the three numbers sequentially
result_1 = get_dynamic_key(user_input_1, "大安")
result_2 = get_dynamic_key(user_input_2, result_1)
result_3 = get_dynamic_key(user_input_3, result_2)

print("\n--- 占卜结果 ---")
print(f"第一步: {result_1} -> {sequence_dict[result_1]}")
print(f"第二步: {result_2} -> {sequence_dict[result_2]}")
print(f"最终结果: {result_3} -> {sequence_dict[result_3]}")