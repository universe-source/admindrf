from rest_framework import serializers

from utils.const_variable import ConstInt

from .models import Book, BookLabel


def author_len(value):
    """ 验证器函数: Validator的简化版 """
    if not isinstance(value, str):
        raise serializers.ValidationError('字段值:{} 不是字符串, 非法'.format(value))
    return value


class BookLabelSerializer(serializers.ModelSerializer):
    """ 书籍分类序列化和反序列化
    @ModelSerializer: 
        1. 根据模型自动生成一组字段
        2. 自动生成序列化验证器, 例如unique_together
        3. 简单实现create/update
    """
    class Meta:
        """ 
        @fields: 能够更好的控制需要输出的字段值
        """
        model = BookLabel 
        fields = ('id', 'name', 'alias', 'description')
        #  exclude = ('created',)


class BookSerializer(serializers.Serializer):
    """ 书籍表序列化: {'name': 'book1', 'booklabel': {'alias': '社科'}} """
    bookid = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=ConstInt.LEN_64, required=True)
    publish = serializers.CharField(max_length=ConstInt.LEN_64, required=True)
    author = serializers.CharField(max_length=ConstInt.LEN_32, required=True,
                                   validators=[author_len])
    booklabel = BookLabelSerializer()
    description = serializers.CharField()

    def create(self, validated_data):
        """ 1.反序列化时调用:
                b = BookSerializer(data)
                b.is_valid()
                用于创建一个 Book 实例, 会自动调用b.save()
            2.最后调用is_valid检查反序列化数据
            3.默认的create/save不支持嵌套对象, 需要rewrite
            4.如果 Book Model本身实现了自定义的管理器类, 则嵌套对象的序列化可能更好处理
        """
        # a. 嵌套对象处理
        booklabel_data = validated_data.pop('booklabel')
        booklabel = BookLabel.objects.get(booklabel_data['id']) 
        if not booklabel:
            booklabel = BookLabel.objects.create(**booklabel_data)
        # b. 外层对象
        return Book.objects.create(booklabel=booklabel, **validated_data)

    def update(self, instance, validated_data):
        """ 反序列化时调用:
            b = BookSerializer(ins, data)
        """
        # a. booklabel对象
        booklabel_data = validated_data.pop('booklabel')
        booklabel = instance.booklabel
        booklabel.alias = booklabel_data.get('alias', booklabel.alias)
        booklabel.description = booklabel_data.get('description', booklabel.description)
        booklabel.save()

        # b. book对象
        instance.name = validated_data.get('name', instance.name)
        instance.publish = validated_data.get('publish', instance.publish)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description, blank=True)
        instance.save()

        return instance

    def save(self):
        """ rewrite函数, 在保存的时候进行日志打印 """
        name = self.validated_data['name']
        print('正在反序列化 Book 对象:{}'.format(name))
        super(BookSerializer, self).save()

    def validate_name(self, nvalue):
        """ 字段级别验证: name, 类似django表单的.clean_name方法 """
        if not isinstance(nvalue, str):
            raise serializers.ValidationError('book: name字段不是一个字符串')
        return nvalue

    def validate(self, bookdata):
        """ 对象级别验证: 验证多个字段 """
        name = bookdata.get('name', '')
        publish = bookdata.get('publish', '')
        if not isinstance(name, str) or not isinstance(publish, str):
            raise serializers.ValidationError('book: 存在非法字段')
        return bookdata
