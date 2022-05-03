# ✨Miraclenote
회의 녹음파일을 통해 자동 키워드 추출 및 브레인스토밍을 지원하는 웹 사이트, **Miraclenote**

# 🐹프로젝트 소개
* Miraclenote는 word2vec과 textrank를 이용하여 자동으로 키워드 추출 및 브레인스토밍을 지원하는 음성인식 프로그램입니다.
* Miraclenote의 main server를 django framework를 통해 구현했습니다.
  * 테스트 시 사용: 128.134.233.125:8080
  * aws에서 운영환경 구성: 13.125.45.17

# 💻 Pipeline

* 개발 환경
![image](https://user-images.githubusercontent.com/57217495/166469725-a50a3a7e-7cd2-4cbf-b915-20ea8d7e76d7.png)

* 운영 환경
![image](https://user-images.githubusercontent.com/57217495/166469885-4b20f12a-3d48-4689-92b4-a12d15bfa3bd.png)

* 프로세스 흐름도
![image](https://user-images.githubusercontent.com/57217495/166471617-a83d6517-0547-4a0b-8dbc-5450a2f36cde.png)

* DB구성
![image](https://user-images.githubusercontent.com/57217495/166471844-93cbe32c-70d2-421a-a5d5-a07815ab23c7.png)
  * 총 3개의 DB 테이블 사용


# 🖋Features

* 활용 알고리즘
  * textrank
    * KeywordSummarizer.train_textrank(self, sents, bias=None):
    * KeywordSummarizer.summarize(self, sents, topk=30): 
    * textrank_w2v_to_vis(texts): 
  * word2vec
    * 사전학습된 word2vec 임베딩 활용
    * word2vec으로 5개의 키워드 각각에 대한 유사 키워드를 14개씩 추출
    
* 활용 프로그램
  * vis.js: Textrank_w2v_to_vis 함수로부터 전달받은 json 형태의 nodes와 edges를 활용하여 vis.js의 네트워크 그래프로 시각화
 
* 보안요구사항 반영
  * 패스워드 암호화
  * 비밀번호 생성규칙 검사
  * csrf 토큰 설정
  * 파일업로드 공격방어
  * 404 에러페이지 설정

# 🙋‍♂️팀원 소개
* 김연진
* 류정화
* 이다은
* 한채림
