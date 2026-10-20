import streamlit as st

sequence_dict = {
     "大安": "（吉）身安、事安，大吉大利，凡事容易成功。",
     "留连": "（凶）运气平平，凡事拖延、纠缠不清、官司或行程受阻。",
     "速喜": "（吉）喜事就在眼前，人快到、信速至，诸事顺利。",
     "赤口": "（凶）易有口舌争执、官非、纠纷、血光或不顺。",
     "小吉": "（吉）行事遇贵人，小有成就，结果平和良好。",
     "空亡": "（凶）最凶之兆，音信全无、落空、失财或徒劳无功。"
}

keys_list = list(sequence_dict.keys())

def get_dynamic_key(user_input, start_key):
    step = user_input - 1 
    start_index = keys_list.index(start_key)
    final_index = (start_index + step) % len(keys_list)
    return keys_list[final_index]

st.title("=== 小六壬 ===")
user_question = st.text_input("问题：", placeholder="请输入你想测算的事项...")

col1, col2, col3 = st.columns(3)
with col1:
    user_input_1 = st.number_input("数字1", min_value=1, max_value=99, value=1, step=1)
with col2:
    user_input_2 = st.number_input("数字2", min_value=1, max_value=99, value=1, step=1)
with col3:
    user_input_3 = st.number_input("数字3", min_value=1, max_value=99, value=1, step=1)

if st.button("开始占卜", type="primary"):
    result_1 = get_dynamic_key(user_input_1, "大安")
    result_2 = get_dynamic_key(user_input_2, result_1)
    result_3 = get_dynamic_key(user_input_3, result_2)
    st.markdown("---")
    st.subheader("--- 占卜结果 ---")
    if user_question:
        st.write(f"**占卜问题：** {user_question}")
     
    st.write(f"第一步: {result_1}")
    st.info(sequence_dict[result_1])
    st.write(f"第二步: {result_2}")
    st.info(sequence_dict[result_2])
    
    st.markdown(f"### 最终结果: **{result_3}**")
    st.info(sequence_dict[result_3])
