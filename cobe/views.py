import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("안녕하세요")

class CobeAPIView(APIView):
    permission_classes = [permissions.AllowAny] # 모든 걸 허용

    def post(self, request):
        """
        계정생성
        """
        if request.method != 'POST':
            return None
        user_data = json.loads(request.body)
        print(user_data)

        user_id = user_data['id']
        password = user_data['password']
        name = user_data['name']

        if len(user_id ) < 5:
            raise ValidationError("id는 5자 이상이어야 합니다.")

        if len(password) < 8:
            raise ValidationError("password 는 8자 이상이어야 합니다.")

        if len(name) == 0:
            raise ValidationError("이름을 입력해주세요.")

        # 유저가 존재하는지 체크
        if User.objects.filter(username=user_id).exists():
            raise ValidationError("이미 존재하는 id 입니다")

        user = User.objects.create_user(
            username=user_id,
            password=password,
            email="",
            first_name=name[0],
            last_name=name[1:]
        )
        print(user)

        member = Member.objects.create(user=user)  # user OneToOne 필드 만들어야 함

        return Response(
            data=json.dumps(user_data, ensure_ascii=False),
            status=status.HTTP_201_CREATED
        )

"""
# 유저를 생성

"""

# member 를 생성

# account 계좌 개설


#1. request body 에서 유저 내용을 꺼낸다.
#2. 사용자 값이 제대로 있는지 확인(검증)
#   id, pw 값이 제대로 있는지 없으면 에러
#3.
# 3-1 ) DB에 똑같은 아이디 있는지 검증 3-2) 유저 만들기 3-3) 멤버객체를 만든다

# GET 현재 계좌 정보 보기 : 계좌에 속한 입금 정보 전부
# select_related -> join
# for payment in account.payments: -> 쿼리 날림...

# POST, CREATE 계좌 개설
# 로그인한 유저의 계좌를 찾아서...

# POST, CREATE PAYMENT 입금
# 로그인한 유저의 계좌를 찾아서... 입금을 한다.

# 커피내역을 확인하고, 내역이 있으면 돈을 주지 않는다
# PUT, DELETE?