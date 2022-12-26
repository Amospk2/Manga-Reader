from django.utils import timezone
import datetime
from django.test import TestCase
from .models import User,Manga,Capitulo,Page,Comment,ForumPost,ForumPostComment

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username = "fulano",
            first_name = "Fulano",
            last_name = "Silva"
        )

    def testUsers(self):
        user = User.objects.get(username="fulano")
        self.assertEqual(user.get_full_name(), "Fulano Silva")

class MangaTesteCase(TestCase):
    def setUp(self):
        Manga.objects.create(
            title = "Manga de testes",
            author = "Mangaka de Testes",
            description = "Lorem ipsum dolor.",
            release_date = datetime.date(2022, 12, 24),
            tags = "Shounen",
        )

    def testManga(self):
        manga = Manga.objects.get(title="Manga de testes")
        self.assertEqual(manga.__str__(), "Manga de testes")
        self.assertEqual(manga.release_date, datetime.date(2022, 12, 24))

class CapituloTestCase(TestCase):
    def setUp(self):
        Manga.objects.create(
            title = "Manga de testes",
            author = "Mangaka de Testes",
            description = "Lorem ipsum dolor.",
            tags = "Shounen",
        )
        Capitulo.objects.create(
            manga = Manga.objects.get(title="Manga de testes"),
            title = "Capítulo de testes",
            description= "Lorem ipsum dolor."
        )

    def testCapitulo(self):
        capitulo = Capitulo.objects.get(title="Capítulo de testes")
        self.assertEqual(capitulo.__str__(), "Capítulo de testes")

class PageTestCase(TestCase):
    def setUp(self):
        Manga.objects.create(
            title = "Manga de testes",
            author = "Mangaka de Testes",
            description = "Lorem ipsum dolor.",
            tags = "Shounen",
        )
        Capitulo.objects.create(
            manga = Manga.objects.get(title="Manga de testes"),
            title = "Capítulo de testes",
            description= "Lorem ipsum dolor."
        )
        Page.objects.create(
            capitulo = Capitulo.objects.get(title="Capítulo de testes"),
            title = "Título da página?"
        )

    def testPage(self):
        page = Page.objects.get(title="Título da página?")
        self.assertEqual(page.capitulo.__str__(), "Capítulo de testes")
        self.assertEqual(page.__str__(), "Título da página?")

class CommentTestCase(TestCase):
    def setUp(self):
        Manga.objects.create(
            title = "Manga de testes",
            author = "Mangaka de Testes",
            description = "Lorem ipsum dolor.",
            tags = "Shounen",
        )
        Capitulo.objects.create(
            manga = Manga.objects.get(title="Manga de testes"),
            title = "Capítulo de testes",
            description= "Lorem ipsum dolor."
        )
        Page.objects.create(
            capitulo = Capitulo.objects.get(title="Capítulo de testes"),
            title = "Título da página?"
        )
        Comment.objects.create(
            page = Page.objects.get(title="Título da página?"),
            title = "Comentário de testes",
            content = "Lorem ipsum dolor."
        )

    def testComment(self):
        comment = Comment.objects.get(page=Page.objects.get(title="Título da página?"))
        self.assertEqual(comment.__str__(), "Comentário de testes")

class ForumPostCase(TestCase):
    def setUp(self):
        ForumPost.objects.create(
            title = "Fórum de testes",
            content = "Lorem ipsum dolor.",
        )

    def testForumPost(self):
        forumPost = ForumPost.objects.get(title="Fórum de testes")
        self.assertEqual(forumPost.publish_date, timezone.now())

class ForumPostCommentCase(TestCase):
    def setUp(self):
        ForumPost.objects.create(
            title = "Fórum de testes",
            content = "Lorem ipsum dolor.",
        )
        ForumPostComment.objects.create(
            forumpost = ForumPost.objects.get(title="Fórum de testes"),
            content = "Lorem ipsum dolor.",
        )

    def testForumPost(self):
        forumPostComment = ForumPostComment.objects.get(
            forumpost = ForumPost.objects.get(title="Fórum de testes")
        )
        self.assertEqual(forumPostComment.publish_date, datetime.date.today())
        