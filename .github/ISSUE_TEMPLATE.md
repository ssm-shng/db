---
title: '[일정 추가] {{ env.EVENT_NAME }}'
labels: 일정 요청(자동)
---
{{ env.DESC }}

날짜: {{ env.YEAR }}년 {{ env.MONTH }}월 {{ env.DAY }}일
종류: {{ env.TAG }}
대상: {{ env.TARGET }}
작성자: {{ env.COMMITTER }}

일정 데이터:
```json event_data
{{ env.EVENT }}
```