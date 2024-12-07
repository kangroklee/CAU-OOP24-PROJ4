from data_loader import DataLoader
from models import User
from cosine_simil import get_similar


def generate_recs(user, media_list, tfidf_matrix):
    """
    사용자 선호도를 기반으로 추천 목록을 생성합니다.

    Args:
        user (User): 사용자 객체
        media_list (list): 미디어 데이터 리스트
        tfidf_matrix: TF-IDF 매트릭스

    Returns:
        list: 추천 미디어 리스트
    """
    if not user.likes:
        print("No preferences found for the user.")
        return []

    liked_indices = [i for i, media in enumerate(media_list) if media.title in {m.title for m in user.likes}]

    all_recommendations = []
    for index in liked_indices:
        similar_items = get_similar(media_list, tfidf_matrix, index)
        all_recommendations.extend(similar_items)

    unique_recommendations = {media.title: media for media in all_recommendations if
                              media.title not in {m.title for m in user.likes}}

    return list(unique_recommendations.values())[:10]


def main():
    """
    프로그램의 메인 함수로 사용자 입력을 받아 추천 시스템을 실행합니다.
    """
    try:
        loader = DataLoader('./movies_metadata.csv')  # 데이터 로더 초기화
        loader.load_data()  # 데이터 로드
        print("Data loaded successfully.")

        print("Choose media type: 1. Movies, 2. TV Shows, 3. Dramas")
        media_type = int(input("Enter your choice (1, 2, 3): "))  # 사용자로부터 미디어 타입 입력 받기
        loader.preprocess(media_type)  # 선택한 미디어 타입의 데이터 전처리

        media_list = loader.media_type  # 선택된 미디어 리스트
        tfidf_matrix = loader.tfidf_matrix  # TF-IDF 매트릭스

        users = {}  # 사용자 데이터 관리

        while True:
            print("\nWelcome! Please choose an option:")
            print("1. Log in")
            print("2. Sign in")
            print("3. Exit")
            choice = input("Enter your choice (1, 2, 3): ").strip()

            if choice == '1':  # Log in
                name = input("Enter your name: ").strip()
                if name in users:
                    print(f"Welcome back, {name}!")
                    user = users[name]

                    # 로그인한 사용자에게 추천 출력
                    print(f"\n{name}'s Preferences:")
                    for media in user.likes:
                        print(f"- {media.title}")

                    print("\nRecommendations for you:")
                    recommendations = generate_recs(user, media_list, tfidf_matrix)
                    if recommendations:
                        for media in recommendations:
                            print(f"- {media.title}")
                    else:
                        print("No recommendations available.")

                else:
                    print(f"No user found with the name '{name}'. Please sign in first.")

            elif choice == '2':  # Sign in
                name = input("Enter your name: ").strip()
                if name in users:
                    print(f"User '{name}' already exists. Please log in instead.")
                    continue

                user = User(name)
                users[name] = user
                print(f"Registration successful! Welcome, {name}!")
                print("\nLet's set up your preferences!")
                print("Enter the titles of the media you like (type 'done' when finished):")
                while True:
                    title = input("Enter a title: ").strip()
                    if title.lower() == 'done':
                        break
                    matching_media = [media for media in media_list if media.title.lower() == title.lower()]
                    if matching_media:
                        user.add_like(matching_media[0])
                        print(f"Added '{title}' to your preferences.")
                    else:
                        print(f"No media found with the title '{title}'. Please try again.")

            elif choice == '3':  # Exit
                print("Thank you for using the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
