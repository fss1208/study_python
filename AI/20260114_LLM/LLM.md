# Large Language Model (LLM)

## 용어 정리
- prompt : 질문
- completion : 답변
- Small Language Model : SLM

## 사용 방법
1. API Key 준비
2. Chat Completion API 사용
3. Chat Completion API 호출
    - model : 모델
    - messages : 메시지 (role, content)

## 파이썬
```python
pip install openai

from openai import OpenAI

client = OpenAI(api_key='your-api-key')

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role": "user", 
            "content": "prompt"
        }
    ]
)

print(response)
```
