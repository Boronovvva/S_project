from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'phone',)

    def get_age(self, obj):
        return obj.age
        
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        max_length = 255, write_only = True
    )

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','date_of_birth',
                  'phone', 'password', 'confirm_password')
        
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            phone = validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError("Пароль должен быть более 8 символов")
        
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        return attrs
