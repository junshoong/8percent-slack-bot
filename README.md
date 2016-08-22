8퍼센트 투자목록 slack bot
=========

##About 8percent
**[8percent 홈페이지](https://8percent.kr)**


## 사용환경
python3
pip3
slack


##설치 및 실행
```
git clone https://github.com/vaporize93/8percent-slack-bot.git
pip3 install -r requirements.txt
```
start.sh 파일 내에 있는 SLACK_TOKEN에 해당 봇의 토큰을 넣고
```
chmod u+x start.sh; ./start.sh
```
로 실행가능 합니다.

##명령
```
list
```
현재 투자목록을 가져옵니다.

```
deal [채권번호]
```
채권번호에 해당하는 세부 내용을 가져옵니다.


##Author
Harvey Kim(vaporize93@gmail.com)
