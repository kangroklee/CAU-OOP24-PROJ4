import time

class BaseTimeEntity:
    """
    모든 객체가 생성된 시간을 기록하는 기본 클래스입니다.
    """
    created_at = time.time()

class Media:
    """
    모든 미디어의 기본 클래스입니다.
    """
    def __init__(self, title, overview):
        self.title = title  # 제목
        self.overview = overview  # 줄거리

class Movie(Media):
    """
    영화 정보를 관리하는 클래스입니다.
    """
    def __init__(self, title, overview, release_year, director):
        super().__init__(title, overview)
        self.release_year = release_year  # 출시 연도
        self.director = director  # 감독 이름

class TVShow(Media):
    """
    TV 프로그램 정보를 관리하는 클래스입니다.
    """
    def __init__(self, title, overview, season):
        super().__init__(title, overview)
        self.season = season  # 시즌 수

class Drama(Media):
    """
    드라마 정보를 관리하는 클래스입니다.
    """
    def __init__(self, title, overview, season):
        super().__init__(title, overview)
        self.season = season  # 시즌 수

class User(BaseTimeEntity):
    """
    사용자를 관리하는 클래스입니다.
    """
    def __init__(self, name):
        self.name = name  # 사용자 이름
        self.likes = set()  # 좋아하는 미디어
        self.watched = set()  # 시청한 미디어

    def add_like(self, media):
        self.likes.add(media)  # 좋아하는 미디어 추가

    def add_watched(self, media):
        self.watched.add(media)  # 시청한 미디어 추가
