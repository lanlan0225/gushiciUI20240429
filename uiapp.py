import streamlit as st
import requests
import json

# 配置你的API Key和Secret Key
API_KEY = 'uQ97TaTUkSZJwc6jKKIpd35V'
SECRET_KEY = 'ur5lIdl0DG0abMuAX4e7OdpVXEUNyFjJ'

# 初始化一个会话，用于保存你的API Key和Secret Key
session = requests.Session()
session.headers.update({
    'Authorization': f'Bearer {API_KEY}',
    'X-Secret-Key': SECRET_KEY
})


def make_request(prompt):
    # 调用千帆大模型平台的API，发送你的请求
    response = session.post('https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro', json={'prompt': prompt})
    return response.json()


def main():
    st.title('千帆大模型对话界面')
    user_input = st.text_input('请输入你的问题：')

    if st.button('发送'):
        # 调用千帆大模型平台，获取响应
        response = make_request(user_input)
        # 显示千帆大模型的响应
        st.write('模型响应：')
        st.write(response['answer'])


if __name__ == '__main__':
    main()