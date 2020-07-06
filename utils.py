from models import Pessoas
from models import Usuarios
from random import randint


def insere_pessoas():
    pessoa = Pessoas(nome="Cardoso", idade=23)
    pessoa.save()
    print(pessoa)


def consulta():
    pessoa = Pessoas.query.all()
    for p in pessoa:
        print(p.id, p.nome, p.idade)


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Andre").first()
    pessoa.idade = 27
    pessoa.nome = "Andre Marques"
    pessoa.save()


def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Cesar Andrade").first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario_db = Usuarios.query.all()
    response = [i.login for i in usuario_db]
    if not (usuario.login in response):
        usuario.save()
        print(usuario)
    else:
        print("Esse usuario já está cadastrado")


def get_usuario():
    usuario = Usuarios.query.all()
    response = [{'id': i.id, 'login': i.login, 'senha': i.senha} for i in usuario]
    print(response, len(response))


def status(status):
    status = status

    print(status)
    if status:
        print("Status concluido")


if __name__ == '__main__':
    insere_usuario("Andre", "123456")
    get_usuario()



