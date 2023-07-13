# sns_toy_project

**SNS 클론**

- 구현해야 하는 기능: 사용자 인증, 포스트 업로드 및 공유, 댓글 및 좋아요 기능, 팔로우 기능
- 난이도: 중급 ~ 고급
- 예상 소요 시간: 약 30시간
- 추가 설명 및 방법: SNS 서비스를 클론함으로써 복잡한 관계를 가진 데이터베이스 구조와, 다양한 유저 인터랙션을 다루는 법을 배울 수 있습니다. 댓글, 좋아요, 팔로우 등의 기능을 구현하면서 Django의 모델 관계와 쿼리를 좀 더 깊게 이해할 수 있습니다.

**사용자 스토리 작성**

1. 사용자로서, 나는 계정을 생성하고 로그인하여 나의 개인정보를 관리할 수 있어야 한다.
2. 사용자로서, 나는 포스트를 작성하고, 수정하고, 삭제할 수 있어야 한다.
3. 사용자로서, 나는 다른 사람의 포스트에 댓글을 남길 수 있어야 한다.
4. 사용자로서, 나는 좋아하는 포스트에 좋아요를 누를 수 있어야 한다.
5. 사용자로서, 나는 다른 사람들을 팔로우하고, 나를 팔로우하는 사람을 확인할 수 있어야 한다.

**기능 목록 생성**

1. 계정 생성, 로그인, 로그아웃 기능
2. 포스트 생성, 수정, 삭제 기능
3. 댓글 생성, 수정, 삭제 기능
4. 좋아요 기능
5. 팔로우 기능

**설계 문서 작성**

1. **기술 스택**: Python, Django, Django REST Framework, SQLite, HTML, CSS, JavaScript
2. **구조**:
    - Back-end: Django를 사용하여 API 서버 구축
    - Front-end: HTML, CSS, JavaScript를 사용하여 간단한 웹 인터페이스 구현
3. **모델 설계**:
    - User: Django의 기본 User 모델 사용. 추가적인 정보 필요시 UserProfile 모델을 생성하여 OneToOneField로 연결.
    - Post: User(작성자), text(포스트 내용), created_at(생성 시간), updated_at(수정 시간)
    - Comment: User(작성자), Post(대상 포스트), text(댓글 내용), created_at(생성 시간)
    - Like: User(좋아요 한 사용자), Post(대상 포스트)
    - Follow: User(팔로우 한 사용자), User(팔로우 당한 사용자)
4. **API 설계**:
    - 계정 관련 API: 로그인, 로그아웃, 계정 생성, 계정 정보 조회 및 수정
    - 포스트 관련 API: 포스트 생성, 수정, 삭제, 포스트 목록 조회
    - 댓글 관련 API: 댓글 생성, 수정, 삭제
    - 좋아요 관련 API: 좋아요 추가, 삭제
    - 팔로우 관련 API: 팔로우 추가, 삭제, 팔로우 목록 조회