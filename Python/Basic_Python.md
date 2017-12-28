# Basic Python

------

## 파일의 실행

- 파이썬을 터미널에서 실행하기 위해서는 아래와 같은 명령어를 입력

  ```powershell
  python file_name.py # 해당 파일의 디렉토리위치까지 들어간 후 입력. 
  ```





## 주석

- 단일라인 # / 복수라인 """

  ```python
  # print("한줄만 주석처리는 #으로 처리합니다")

  """
  print("여러줄의 주석은")
  print("따옴표 3개로 감싸서 처리합니다.")
  """

  ```





## 변수

- 변수명 = '값'

  ```python
   # 값의 타입에 따라 변수의 타입이 자동으로 변환
  str_name = 'rakk'
  int_first = 7
  int_second = 6
  ```

- 변수의 활용

  ```python
  print('안녕하세요 ',  str_name, '입니다.')
  @출력결과 : 안녕하세요 rakk 입니다.
  ```

- 숫자와 문자열 변수의 차이점

  - 숫자의 경우 사칙연산이 가능하지만 문자열의 경우 이어붙여줌

  ```python
  print(int_first + int_second)
  @출력결과 : 13

  int_first = '7'
  int_second = '6'
  print(str_name + int_name)
  @출력결과 : 76
  ```





## if문

- **if문의 기본적인 포맷** 

  - if문의 다음 줄은 반드시 ***들여쓰기***

  ```python
  # 올바른 사용법
  if 조건식 :
      print()
      print()
      print()
      
  # 잘못된 사용법 - 오류발생
  if 조건식 :
      print()
    print()
         print()
  ```

  - if문의 블럭관계 - 들여쓰기의 중요성

  ```python
  if True:
      print('조건1')
      if False:
          print('조건2')
      print('조건3')
  #조건3의 명령어는 첫 번째 if문의 소속
  @실행결과 : 조건1
      	   조건3
  ```

  > 조건 :  < , > , <= , >=, ==, !=

  > boolean : and , or , not 

- **if-else / elif기본적인 포맷**

  ```python
  if 조건식1:   
      code
  elif 조건식2:   
      code
  else:   
      code
  ```





## 함수와 매개변수

> 자바의 class와 유사한 기능

- **함수의 정의**

  ```python
  #함수 선언
  def function():
  	print("안녕, 함수")
      
  #함수의 사용법
  function()
  @실행결과 : 안녕, 함수
  ```

  ​