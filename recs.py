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

