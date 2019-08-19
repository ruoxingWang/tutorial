from ..models import Snippet
from ..serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()
snippet = Snippet(code='print "hello, world"\n')
snippet.save()

#实例序列化。
serializer = SnippetSerializer(snippet)
serializer.data

content = JSONRenderer().render(serializer.data)
content

# 反序列化 解析为Python dict数据类型...
from django.utils.six import BytesIO
stream = BytesIO(content)
data = JSONParser().parse(stream)

# dict数据类型恢复成正常的对象实例
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.save()

from collections import Iterable
# 序列化多个
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data

