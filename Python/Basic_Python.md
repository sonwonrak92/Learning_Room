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

- **매개변수 사용**

  ```python
  def print_root(a, b, c):
      r1 = a * b+c
      
  print_root(1, 2, 3) #정의한 함수에 맞는 매개변수를 넣어줘야함.
  ```

- **format 함수 사용**

  ```python
  name = '락'
  color = '딸기'
  print(' 제 이름은 {}이고 좋아하는 과일은 {}입니다.'.format(name, color ))

  str1 = "{}와 {}는 동물입니다".format(고양이, 강아지)

  # format함수의 매개변수 순서대로 대괄호와 연결
  ```

- **사용자 입력 함수**

  ```python
  input() #자바의 scanner와 같은 기능
  ```



## 리스트

> 다수의 값을 담을 수 있는 변수 / 자바의 배열과 비슷한 기능

```python
list1 = ['a', 'b', 'c', 'd']
list2 = [10, 20, 30, 40 ]

print(list1)
@실행결과 : ['a', 'b', 'c', 'd']

print(list2)
@실행결과 : [10, 20, 30, 40 ]

print(list1[1])
@실행결과 : b
    
print(list1[-1])     #-의 경우 역방향으로 진행
@실행결과 : d

```

- 리스트 값 추가

  ```python
  list1 = [1, 2, 3]

  #기존의 리스트에 4 추가
  list1.append(4)
  print(list1)
  @실행결과 :  [1, 2, 3, 4]
      
  #리스트에 원소하나 추가하여 새로운 리스트생성
  list2 = list1 + [5]    
  print(list2)
  @실행결과 : [1, 2, 3, 4, 5]

  #리스트에 리스트를 추가하여 새로운 리스트생성
  list3 = list1 + list2
  print(list3)
  @실행결과 : [1, 2, 3, 4, 1, 2, 3, 4]
  ```

- 리스트 값 삭제

  ```python
  #특정 위치의 값 삭제
  del list1[2] 

  #특정 값 지우기 - 중복값이 있을 경우 가장 첫값을 지움
  list1.remove(3)
  ```

  ​