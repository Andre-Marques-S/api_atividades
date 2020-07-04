from models import Pessoas


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


if __name__ == '__main__':
    exclui_pessoas()
    consulta()


