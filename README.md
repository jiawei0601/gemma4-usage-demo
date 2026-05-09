# Gemma 4 Demo 專案

本專案展示如何使用 Google 最新的 **Gemma 4** 多模態開源模型。

## 模型介紹
Gemma 4 是由 Google DeepMind 開發的下一代開放權重模型，具備以下亮點：
- **多模態能力**：支援文字、圖片輸入 (E2B/E4B 甚至支援音訊)。
- **Agentic 優化**：特別強化了推理與多步驟計畫能力。
- **超長上下文**：支援最高 256K tokens。

## 如何開始

### 1. 使用 Ollama (本地運行)
這是最簡單的方式，適合想要在自己電腦運行的開發者。

1. [下載並安裝 Ollama](https://ollama.com/)。
2. 在終端機執行：
   ```bash
   ollama run gemma4:e2b
   ```

### 2. 使用 Python 調用 (Ollama SDK)
如果你想在程式中整合 Gemma 4：

1. 安裝套件：
   ```bash
   pip install ollama
   ```
2. 執行本專案的 `app.py`：
   ```bash
   python app.py
   ```

### 3. 使用 Google AI Studio (API 存取)
如果你沒有強大的 GPU，可以使用 Google 的雲端 API：
1. 前往 [Google AI Studio](https://aistudio.google.com/)。
2. 獲取 API Key。
3. 選擇 `gemma-4` 模型進行測試。

## 專案結構
- `app.py`: 簡單的 Python 調用範例。
- `requirements.txt`: 專案依賴。
