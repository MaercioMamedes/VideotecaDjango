# Projeto Videoteca Django

Esse projeto é uma demonstração inicial das minha habilidades como desenvolvedor web, utilizando
a linguagem python e o framework Django. Sendo aplicação CRUD, que acessa a api do [The Movie Data Base](https://www.themoviedb.org/documentation/api) e coleta alguns dados de filmes.

Por questão de segurança a API KEY de acesso à base de dados do The MovieDB, está protegida, por uma variável de ambiente. Para que seja rodar em sua máquina realize o cadastro de uma chave pessoal e insira no arquivo `core/helpers/apiMovieDB.py`, no atributo `self.api_key`.

A chave secreta do projeto que está no arquivo `VideotexaDjango/settings.py` na variável `SECRET_KEY`, também está protegida por variável de ambiente. Para rodar a aplicação insira uma chave de segurança, de sua preferência, na variável mensionada.

As dependências do projeto estão listadas no arquivo requirements.txt e a  versão do Python utilizada foi a 3.10.

## Algumas funcionalidades da aplicação

### Cadastro de Usuário
![](https://github.com/MaercioMamedes/VideotecaDjango/blob/master/docs/pagina-cadastro.png?raw=true)

### CRUD de posters de filmes

![](https://github.com/MaercioMamedes/VideotecaDjango/blob/master/docs/pagina-filmes-favoritos.png?raw=true)

### Autenticação de usuário

![](https://github.com/MaercioMamedes/VideotecaDjango/blob/master/docs/pagina-login.png?raw=true)
