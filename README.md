### **전체적인 구조 정리**

#### **1. 주요 컴포넌트**
구조는 크게 4개의 주요 컴포넌트로 구성됩니다:
1. **데이터 로드 및 전처리** (`DataLoader`)
2. **모델 및 데이터 구조** (`Models`)
3. **추천 알고리즘** (`Recommendation`)
4. **코사인 유사도 계산** (`CosineSimilarity`)

---

### **2. 컴포넌트별 역할**

#### **(1) 데이터 로드 및 전처리 (`DataLoader`)**
- **책임**: 
  - CSV 파일에서 데이터를 로드하고, `Media` 객체와 그 하위 클래스로 변환.
  - 미디어 데이터(`Movie`, `TVShow`, `Drama`)를 각자의 리스트에 저장.
  - 선택된 미디어 타입 데이터를 TF-IDF로 전처리.
- **주요 메서드**:
  - `load_data()`: 데이터를 읽고 결측값을 처리하여 미디어 객체를 생성.
  - `preprocess(media_type)`: 특정 미디어 타입을 선택하고 TF-IDF 벡터화.

#### **(2) 모델 및 데이터 구조 (`Models`)**
- **책임**:
  - 미디어(`Media`)와 사용자(`User`)의 기본 구조를 정의.
  - `Media` 클래스는 `Movie`, `TVShow`, `Drama` 클래스로 확장.
  - `User` 클래스는 사용자가 좋아하는 미디어와 시청한 미디어를 관리.
- **주요 클래스**:
  - **`Media`**: 공통 속성(`title`, `overview`)을 가진 기본 미디어 클래스.
  - **`Movie`, `TVShow`, `Drama`**:
    - `Movie`: 출시 연도(`release_year`), 감독(`director`).
    - `TVShow`, `Drama`: 시즌(`season`).
  - **`User`**:
    - 속성: `likes`(좋아하는 미디어), `watched`(시청한 미디어).
    - 메서드: `add_like(media)`, `add_watched(media)`.

#### **(3) 추천 알고리즘 (`Recommendation`)**
- **책임**:
  - 사용자의 선호도(`likes`)와 시청 기록(`watched`)을 기반으로 추천을 생성.
  - 코사인 유사도(`CosineSimilarity`)를 활용해 유사한 미디어를 추천.
- **주요 함수**:
  - `generate_recs(user, media_list, tfidf_matrix)`:
    - 사용자의 선호도를 가중치로 설정해 추천 목록 생성.
    - `likes` 가중치: 3, `watched` 가중치: 1.

#### **(4) 코사인 유사도 계산 (`CosineSimilarity`)**
- **책임**:
  - 미디어 간의 유사도를 계산.
- **주요 함수**:
  - `calculate_similarity(tfidf_matrix)`: TF-IDF 매트릭스를 사용해 유사도 계산.
  - `get_similar(media_list, tfidf_matrix, target_index)`:
    - 특정 미디어와 유사한 미디어 10개 반환.

---

### **3. 주요 클래스 및 함수 간 관계**

#### **(1) `DataLoader`와 `Media`**
- `DataLoader`는 `load_data()`에서 `Media` 클래스와 하위 클래스(`Movie`, `TVShow`, `Drama`)를 사용해 데이터를 객체로 변환.

#### **(2) `User`와 `Media`**
- `User`는 `add_like` 및 `add_watched` 메서드를 통해 `Media` 객체와 상호작용.

#### **(3) `generate_recs`와 `CosineSimilarity`**
- `generate_recs`는 사용자의 선호도와 시청 기록을 기반으로 `CosineSimilarity` 함수(`get_similar`)를 호출해 추천 결과를 생성.

#### **(4) `DataLoader`와 `CosineSimilarity`**
- `DataLoader`에서 전처리된 TF-IDF 매트릭스를 `CosineSimilarity`가 활용해 유사도 계산.

---

### **4. 실행 흐름**

#### **1단계: 데이터 로드**
- `DataLoader.load_data()`를 호출해 데이터를 로드하고, 결측값을 처리한 뒤 `Media` 객체로 변환.

#### **2단계: 데이터 전처리**
- 사용자 입력을 받아 `DataLoader.preprocess(media_type)`으로 선택한 미디어 타입을 TF-IDF로 변환.

#### **3단계: 사용자 생성**
- `User` 객체를 생성하고, 사용자의 선호도(`likes`)와 시청 기록(`watched`)을 추가.

#### **4단계: 추천 생성**
- `generate_recs()` 함수에서 코사인 유사도를 활용해 추천 결과를 반환.

#### **5단계: 결과 출력**
- 추천된 미디어 목록의 제목(`title`)을 출력.
