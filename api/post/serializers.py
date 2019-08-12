from rest_framework.serializers import ModelSerializer

from Post.models import Post, Files


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')

    def create(self, validated_data):
        p = Post(**validated_data)
        p.save()
        filelist = self.context['request'].FILES.getlist('file')
        for file in filelist:
            f = Files.objects.create(file=file,file_user=p)
            f.save()
        return p

