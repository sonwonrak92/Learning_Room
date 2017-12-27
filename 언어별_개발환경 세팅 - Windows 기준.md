# 개발환경 세팅 - Windows 기준

## ABAP

- ALV, UI5 , HANA DB MODELING , HCP

## Java 

- **JDK(Java Development Kit) 설치**

  - jdk를 설치하면 jre까지 자동으로 설치됩니다.

    > JDK설치 링크 :  http://www.oracle.com/technetwork/java/javase/downloads/index.html

  - 설치 확인 - cmd창에서 아래의 코드를 입력합니다.

    ```bash
    java -version
     # 명령어를 실행하면 바로 아래줄에 버전이 나타나게 됩니다.
     # 버전이 나타나지 않았다면 설치가 올바르게 되지 않은 것입니다.
    ```

- **이클립스 설치 - IDE**

  > 이클립스 설치 링크 : http://www.eclipse.org/users/

  - Eclipse for Jave EE 버전으로 설치 - 어플리케이션 프로젝트를 위해서
    - for Java developers 버전은 단순한 프로그래밍 수준의 가벼운 버전
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

## Ruby

- 크롤링 , 웹사이트

## Python

- 데이터분석

## Kotlin

- 안드로이드개발

