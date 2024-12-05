from cosine_simil import get_similar

def generate_recs(user, media_list, tfidf_matrix):
    """
    사용자의 선호도와 시청 기록을 기반으로 추천 목록을 생성합니다.
    
    Args:
        user: User 객체
        media_list: 미디어 객체 리스트
        tfidf_matrix: TF-IDF 매트릭스
    
    Returns:
        추천 미디어 객체 리스트
    """
    user_preference = {}
    for media in user.likes:
        user_preference[media] = 3  # 좋아하는 미디어는 가중치 3
    for media in user.watched:
        user_preference[media] = 1  # 시청한 미디어는 가중치 1

    recommendations = []
    for media, _ in sorted(user_preference.items(), key=lambda item: item[1], reverse=True):
        target_index = media_list.index(media)  # 미디어의 인덱스 찾기
        recommendations.extend(get_similar(media_list, tfidf_matrix, target_index))  # 유사한 미디어 추가

    return recommendations[:10]  # 상위 10개 반환
