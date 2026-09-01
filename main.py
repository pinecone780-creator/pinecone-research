import os
from dotenv import load_dotenv
from pinecone import Pinecone

# 1. .env 파일의 환경 변수 로드
load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

# 2. API 키 유효성 확인
if not api_key or "여기에" in api_key:
    print("❌ [.env] 파일에 실제 PINECONE_API_KEY를 입력해 주세요.")
else:
    try:
        # 3. Pinecone 클라이언트 연결
        pc = Pinecone(api_key=api_key)
        
        # 4. 인덱스 목록 조회
        indexes = pc.list_indexes()
        index_names = [idx.name for idx in indexes]
        
        print("🎉 Pinecone 데이터베이스에 성공적으로 연결되었습니다!")
        print(f"현재 보유 중인 인덱스 목록: {index_names}")
        
    except Exception as e:
        print(f"❌ 연결 실패: {e}")