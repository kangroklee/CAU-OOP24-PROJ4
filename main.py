from data_loader import DataLoader
from models import User
from recs import generate_recs

def main():
    """
    프로그램의 메인 함수로 사용자 입력을 받아 추천 시스템을 실행합니다.
    """
    loader = DataLoader('./movies_metadata.csv')  # 데이터 로더 초기화
    loader.load_data()  # 데이터 로드

    print("Choose media type: 1. Movies, 2. TV Shows, 3. Dramas")
    media_type = int(input("Enter your choice (1, 2, 3): "))  # 사용자로부터 미디어 타입 입력 받기
    loader.preprocess(media_type)  # 선택한 미디어 타입의 데이터 전처리

    media_list = loader.media_type  # 선택된 미디어 리스트
    tfidf_matrix = loader.tfidf_matrix  # TF-IDF 매트릭스

    user = User("Alice")  # 사용자 생성
    user.add_like(media_list[0])  # 사용자가 좋아하는 미디어 추가 (예제)
    user.add_watched(media_list[1])  # 사용자가 시청한 미디어 추가 (예제)

    recommendations = generate_recs(user, media_list, tfidf_matrix)  # 추천 목록 생성
    print("Recommendations:")
    for media in recommendations:
        print(media.title)  # 추천 미디어의 제목 출력

if __name__ == "__main__":
    main()
