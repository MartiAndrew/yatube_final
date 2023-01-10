from django.test import TestCase
from ..models import Group, Post, User, Comment, NUM_SYMB


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Andrey')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )

    def test_models_have_correct_post_names(self):
        """Проверяем корректность работы __str__."""
        post = PostModelTest.post
        expected_object_name = post.text[:NUM_SYMB]
        self.assertEqual(expected_object_name, str(post))

    def test_models_have_correct_group_names(self):
        """Проверяем корректность работы __str__."""
        group = PostModelTest.group
        expected_group_name = group.title
        self.assertEqual(expected_group_name, str(group))

    def test_title_label(self):
        post = PostModelTest.post
        field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'group': 'Группа',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_value
                )

    def test_post_help_text(self):
        """Проверяем, help_text'ы у модели Post."""
        post = PostModelTest.post

        field_help_texts = {
            'text': 'Введите текст поста',
            'group': 'Выберите группу',
        }

        for field, expected_help_text in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).help_text, expected_help_text
                )


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Andrey')
        cls.post = Post.objects.create(
            text='Тестовый пост',
            author=cls.user,
        )
        cls.comment = Comment.objects.create(
            text='Комментарий для поста',
            author=cls.user,
            post=cls.post,
        )

    def test_сomment_str(self):
        """Проверка __str__ у сomment."""
        comment = CommentModelTest.comment
        expected_object_name = comment.text[:NUM_SYMB]
        self.assertEqual(expected_object_name, str(comment))

    def test_сomment_verbose_name(self):
        """Проверка verbose_name у сomment."""
        field_verboses = {
            'post': 'Пост',
            'author': 'Автор',
            'text': 'Комментарий',
            'created': 'Создан',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.comment._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)

    def test_post_help_text(self):
        """Проверяем, help_text'ы у модели Comment."""
        comment = CommentModelTest.comment
        self.assertEqual(
            comment._meta.get_field('text').help_text, 'Добавить комментарий'
        )
