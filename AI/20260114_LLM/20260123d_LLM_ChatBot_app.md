# 20260123d_LLM_ChatBot_app.py 코드 설명

이 프로그램은 **Streamlit과 LangChain을 활용하여 업로드한 PDF 문서의 내용을 바탕으로 대화를 나누는 시각적인 대화형 챗봇**입니다. 이전에 분석한 코드보다 채팅 인터페이스(`streamlit-chat`)를 활용하여 더 실제 채팅 앱과 유사한 UI를 제공합니다.

---

### 주요 기능 및 코드 구조

#### 1. 환경 설정 및 초기화 (1~15행)
*   **환경 변수**: `dotenv`를 통해 OpenAI API 키를 로드합니다.
*   **컴포넌트**: `streamlit_chat`의 `message` 함수를 사용하여 말풍선 형태의 채팅 UI를 구현합니다.
*   **임시 파일**: `tempfile`을 사용하여 업로드된 PDF를 시스템에 임시로 저장한 뒤 로드합니다.

#### 2. PDF 로드 및 인덱싱 (17~30행)
*   **PyPDFLoader**: LangChain의 내장 로더를 사용하여 PDF를 페이지 단위 문서 객체(`data`)로 변환합니다.
*   **임베딩**: `OpenAIEmbeddings`를 사용하여 문서 내용을 벡터화합니다.
*   **FAISS**: 벡터 데이터를 메모리 기반 검색 엔진에 저장합니다.
*   **ConversationChain**: LLM(`gpt-4.1-mini`)과 검색기(Retriever)를 연결하여 대화 체인을 생성합니다.

#### 3. 대화 처리 로직 (`conversational_chat`) (32~35행)
*   사용자의 질문과 `st.session_state`에 저장된 과거 대화 이력(`history`)을 함께 LLM에 전달합니다.
*   생성된 답변을 다시 `history`에 추가하여 대화의 문맥(Context)을 유지합니다.

#### 4. 세션 상태(Session State) 관리 (37~45행)
*   `history`: LLM이 문맥을 이해하기 위한 (질문, 답변) 튜플 리스트.
*   `generated`: 화면에 표시할 챗봇의 응답 리스트.
*   `past`: 화면에 표시할 사용자의 질문 리스트.

#### 5. 채팅 UI 구성 (47~66행)
*   **Layout**: `st.container`를 각각 응답 내용과 입력창용으로 나누어 구성합니다.
*   **입력 폼**: `st.form`을 사용하여 질문을 입력하고 전송 버튼을 누르면 화면이 새로고침되며 메시지가 처리됩니다.
*   **메시지 렌더링**: `streamlit_chat` 라이브러리를 통해 사용자(`is_user=True`)와 봇의 메시지를 구분하고 아바타 스타일(`fun-emoji`, `bottts`)을 적용하여 출력합니다.

---

### 이전 버전(app.py)과의 차이점
1.  **UI 라이브러리**: 일반적인 `st.write` 대신 `streamlit-chat`을 사용하여 더 풍부한 채팅 인터페이스를 제공합니다.
2.  **로딩 방식**: `PyPDF2`로 직접 텍스트를 추출하는 대신 LangChain의 `PyPDFLoader`를 사용합니다.
3.  **데이터 처리**: 텍스트를 수동으로 자르는 과정 없이 문서 객체(`Document`)를 그대로 FAISS에 전달합니다.

### 프로그램 흐름
1.  **Sidebar**: PDF 파일 업로드 및 데이터 처리.
2.  **Input Form**: 사용자가 질문을 입력하고 'Send' 클릭.
3.  **RAG Process**: 기존 대화 이력과 질문을 결합하여 검색 후 답변 생성.
4.  **Display**: 전체 대화 내역을 루프를 돌며 말풍선 형태로 화면에 출력.
