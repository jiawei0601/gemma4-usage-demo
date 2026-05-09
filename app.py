import ollama

def chat_with_gemma4():
    print("正在與 Gemma 4 連線 (請確保 Ollama 已啟動)...")
    try:
        # 文字聊天範例
        response = ollama.chat(model='gemma4:e2b', messages=[
            {
                'role': 'user',
                'content': '請用繁體中文自我介紹，並說明你作為 Gemma 4 的核心優勢。',
            },
        ])
        print("\nGemma 4 回覆：\n")
        print(response['message']['content'])

        # 多模態 (圖片) 範例註釋
        """
        # 如果你想讓 Gemma 4 辨識圖片，可以這樣寫：
        with open('image.jpg', 'rb') as f:
            response = ollama.chat(
                model='gemma4:e2b',
                messages=[{'role': 'user', 'content': '這張圖裡面有什麼？', 'images': [f.read()]}]
            )
        print(response['message']['content'])
        """
    except Exception as e:
        print(f"錯誤：{e}")
        print("提示：請確保已安裝 Ollama 並執行 `ollama pull gemma4:e2b`。")

if __name__ == "__main__":
    chat_with_gemma4()
