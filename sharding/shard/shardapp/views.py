from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from django.views import View
from . import models
from rest_framework import serializers

# Create your views here.

class Index(APIView):
    def post(self,request):
        client = request.data['client']   
        score = request.data['score']

        if score.isdigit() and int(score)<10000000:
            models.Message.objects.create(
                name = client,
                score = score
            )
            return JsonResponse({
                'code':200,
            })
            
        else:
            return JsonResponse({
                'code':500,
                'message':'输入有误'
            })

class MessageSer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"


class Order(APIView):
    def post(self,request):
        message = models.Message.objects.order_by('-score')
        message_data = MessageSer(instance=message, many=True)
        query_name = request.data.get('query_name')
        # 判断字端范围，数字，是否为数据库字段，
        if query_name:
            count = models.Message.objects.all().count()
            search = models.Message.objects.filter(name=query_name).all()
            if query_name.isdigit() and int(query_name)<=count:
                query_range = [int(query_name)]
                return JsonResponse({
                    'code':200,
                    'query_range':query_range
                })
            else:
                if "~" in query_name:
                    range = query_name.split('~')
                    try:
                        query_range = [int(range[0]),int(range[1])]
                        return JsonResponse({
                            'code':200,
                            'query_range':query_range
                        })
                    except:
                        return JsonResponse({
                            'code':500,
                            'error':"输入错误"
                        }) 
                else:
                    return JsonResponse({
                        'code':500,
                        'error':"输入错误"
                    }) 
        else:
            pass
        return JsonResponse({
            'code':200,
            'messagelist':message_data.data
        })
   






class Test_Order_By(APIView):
    """
    取出数据进行排序
    a2 返回给前端排序后的数据
    test1 当前用户的数据
    test3 得到所有数据的长度列表
    
    """
    def get(self,request):
        name = request.GET.get('name')
        test1 = models.Test.objects.get(name=name)

        test2 = models.Test.objects.order_by('-score')

        test3 = [str(i) for i in range(1,len(test2)+1)]

        a2=dict(zip(test3,test2)) 
     
        return render(request,'test_order_by.html',locals())