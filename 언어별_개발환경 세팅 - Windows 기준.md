# 개발환경 세팅 - Windows 기준

## IDE -[ MS VScode설치 ] 

**VScode 설치 - IDE**

> VS cod설치 링크 : https://code.visualstudio.com/

- python 플러그인 설치 
  - 확장열기[ctrl+shift+x] - 마켓플레이스검색창에 python입력 후 설치

------

## ABAP

- ALV, UI5 , HANA DB MODELING , HCP

------

## Java 

- **JDK(Java Development Kit) 설치**

  - jdk를 설치하면 jre까지 자동으로 설치됩니다.

    > JDK설치 링크 :  http://www.oracle.com/technetwork/java/javase/downloads/index.html

  - 설치 확인 - cmd창에서 아래의 명령어를 입력

    ```bash
    java -version
     # 명령어를 실행하면 바로 아래줄에 버전이 나타나게 됩니다.
     # 버전이 나타나지 않았다면 설치가 올바르게 되지 않은 것입니다.
    ```

- **이클립스 설치 - IDE**

  > 이클립스 설치 링크 : http://www.eclipse.org/users/

  - Eclipse for Jave EE 버전으로 설치 - 어플리케이션 프로젝트를 위해서

    for Java developers 버전은 단순한 프로그래밍 수준의 가벼운 버전

  - 이클립스 설치 완료 후 jdk를 default값으로 설정하기 위한 작업필요
    - window - preferences - java - installed JREs - add - standard vm - dictionary - jdk폴더선택

  - encoding의 경우 utf-8으로 설정하는 것을 추천

- **Hello World 출력해보기**

  ```java
  public class HelloWorld{
    public static void main(String[] args)
      System.out.println("Hello, World")
  }
  ```

  ​

------

## Ruby on rails

- **루비 설치**

  > 루비 설치 링크 : https://www.ruby-lang.org/ko/downloads/


- **rails 설치**

  - 루비 설치 후 ruby prompt를 실행, 아래의 명령어 입력

    ```ruby
    gem install rails
    ```

    ​

------

## Python

- **파이썬 설치** 

  > 파이썬 설치 링크 : [www.python.org](http://www.python.org/)

  - 인스톨 진행 중 path 체크 필수
  - 설치 확인 - cmd창에서 아래의 명령어를 입력

  ```bash
  python
   # 명령어를 실행하면 바로 아래줄에 버전이 나타나게 됩니다.
   # 버전이 나타나지 않았다면 설치가 올바르게 되지 않은 것입니다.
  ```

- **Hello World 출력해보기**

  ```python
  print("Hello, World")
  ```

  ​

------

## Kotlin

- 안드로이드개발.

