import pandas as pd
from models import Movie, TVShow, Drama

class DataLoader:
    def __init__(self, file_path):
        """
        초기화 메서드: 데이터 파일 경로와 각 미디어 타입의 리스트를 초기화합니다.
        """
        self.file_path = file_path
        self.movies = []  # Movie 객체 리스트
        self.tv_shows = []  # TVShow 객체 리스트
        self.dramas = []  # Drama 객체 리스트
        self.tfidf_matrix = None  # TF-IDF 매트릭스를 저장
        self.media_type = None  # 현재 선택된 미디어 타입 리스트

    def load_data(self):
        """
        데이터 파일을 읽어 미디어 객체(Movie, TVShow, Drama)로 변환합니다.
        """
        # CSV 파일 로드
        data = pd.read_csv(self.file_path, low_memory=False)
        
        # 'overview'와 'release_date'의 결측값 처리
        data['overview'] = data['overview'].fillna('')  # 줄거리 공백 처리
        data['release_date'] = data['release_date'].fillna('0000-00-00')  # 출시 날짜 기본값 설정

        # Movie 객체 생성 (1~1000행)
        self.movies = [
            Movie(row['title'], row['overview'], int(str(row['release_date'])[:4]), "Unknown")
            for _, row in data[:1000].iterrows()
            if pd.notna(row['title'])  # 제목이 결측값인 경우 건너뜀
        ]

        # TVShow 객체 생성 (1001~2000행)
        self.tv_shows = [
            TVShow(row['title'], row['overview'], season=1)
            for _, row in data[1000:2000].iterrows()
            if pd.notna(row['title'])  # 제목이 결측값인 경우 건너뜀
        ]

        # Drama 객체 생성 (2001~3000행)
        self.dramas = [
            Drama(row['title'], row['overview'], season=1)
            for _, row in data[2000:3000].iterrows()
            if pd.notna(row['title'])  # 제목이 결측값인 경우 건너뜀
        ]

    def preprocess(self, media_type):
        """
        선택한 미디어 타입의 데이터를 TF-IDF로 전처리합니다.
        """
        if media_type == 1:
            # 영화 데이터를 선택
            corpus = [media.overview for media in self.movies]
            self.media_type = self.movies
        elif media_type == 2:
            # TV 프로그램 데이터를 선택
            corpus = [media.overview for media in self.tv_shows]
            self.media_type = self.tv_shows
        elif media_type == 3:
            # 드라마 데이터를 선택
            corpus = [media.overview for media in self.dramas]
            self.media_type = self.dramas
        else:
            # 잘못된 입력 처리
            raise ValueError("Invalid media type. Choose 1, 2, or 3.")

        # TF-IDF 매트릭스 생성
        from sklearn.feature_extraction.text import TfidfVectorizer
        tfidf = TfidfVectorizer(stop_words='english')  # 영어 불용어 제거
        self.tfidf_matrix = tfidf.fit_transform(corpus)
