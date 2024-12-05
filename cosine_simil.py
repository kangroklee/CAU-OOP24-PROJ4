from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(tfidf_matrix):
    """
    TF-IDF 매트릭스를 이용해 코사인 유사도를 계산합니다.
    """
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_similar(media_list, tfidf_matrix, target_index):
    """
    특정 미디어와 유사한 미디어 목록을 반환합니다.
    
    Args:
        media_list: 미디어 객체 리스트
        tfidf_matrix: TF-IDF 매트릭스
        target_index: 타겟 미디어의 인덱스
    
    Returns:
        유사한 미디어 객체 리스트
    """
    cosine_sim = calculate_similarity(tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[target_index]))  # 타겟 미디어와 다른 모든 미디어의 유사도
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]  # 상위 10개 유사도

    return [media_list[i[0]] for i in sim_scores]  # 유사한 미디어 반환
