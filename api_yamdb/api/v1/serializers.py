from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация модели Category."""

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    """Сериализация модели Genre."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleWriteSerializer(serializers.ModelSerializer):
    """Сериализация модели Title для записи."""
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         many=True,
                                         slug_field='slug')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')

    class Meta:
        model = Title
        fields = '__all__'


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериализация модели Title только для чтения."""
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class UserSignUpSerializer(serializers.ModelSerializer):
    """Сериализация данных при регистрации пользователя."""

    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=(
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким username уже существует'
            ),
        )
    )
    email = serializers.EmailField(
        max_length=254,
        required=True,
        validators=(
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким email уже существует'),
        )
    )

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError(
                'Невозможно создать пользователя с логином me'
            )
        return value

    def validate_email(self, value):
        lowe_case_value = value.lower()
        if User.objects.filter(email=lowe_case_value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email существует.'
            )
        return lowe_case_value


class TokenSerializer(serializers.Serializer):
    """Сериализация токена."""

    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    """Сериализация модели User."""

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'bio', 'role')


class UserMeSerializer(serializers.ModelSerializer):
    """Сериализация модели User."""

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'bio', 'role')
        read_only_fields = ('role',)


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация модели Review."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    score = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('title',)

    def validate(self, data):
        author = self.context['request'].user
        title_id = self.context['view'].kwargs.get('title_id')
        if self.context['request'].method == 'POST':
            if Review.objects.filter(title__id=title_id,
                                     author=author).exists():
                raise serializers.ValidationError(
                    'Можно оставить только один отзыв на произведение')
        return data

    def validate_integer_number(self, score):
        if score > 10 or score < 1:
            raise serializers.ValidationError(
                'Выберете оценку от 1 до 10')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
