
# Leitor de manga feito em Django/Python

Projeto de um leitor de mangas feito utilizando html, css, js e python como ferramentas. As tecnologias deste projeto:

- Django(Python)
- Template engine
- html, css e js para o front-end

# Conheçendo o projeto

Este projeto, como o nome diz, se trata de um site para a leitura de mangas. Dentre as funcionalidades ele permite a criação de mangas, de capítulos para esses mangas, criação de usuários e o gerenciamento tanto de mangas quanto e usuários do sistema.

Além disso, o site conta com um fórum que permite que os usuários coloquem suas duvidas e reclamações. O objetivo principal deste site foi adquirir conhecimentos na tecnologia principal, Django, e além disso utilizar de tecnologias pra desenvolvimento em grupo.

Utilizando o Notion criei uma rotina de desenvolvimento, criando as tasks e atribuindo a todos que participaram do processo de desenvolvimento. Esse projeto também  foi importante para entender melhor o desenvolvimento web com o python, lidando com problemas reais e resolvendo problemas maiores usando essa linguagem que tanto gosto.


# Rodando o projeto

  
Para rodar o projeto, verifique se o python está instalado e depois execute no terminal:

1: Criando o virtual environment:
*`python -m venv env`* 

2: Instalando os packages do projeto, ative o virtual environment e depois execute:
*`pip install -r requirements.txt`*

3: Rode as migrations(modelos do banco):
*`python manage.py migrate`*

4: Para iniciar o projeto:
*`python manage.py runserver`*
  

**Area Dev: É altamente recomendavel configurar um usuário Root para o acessar os paineis do Django!**

1:  Criando um super usuário:
*`python manage.py createsuperuser`* - informe usuário, email e senha

# Screenshots

Algumas referências da aparência do site:

![home](/imgs/img0.png)

![gif](/imgs/gif0.gif)

![feed](/imgs/img1.png)

![feed](/imgs/img2.png)
