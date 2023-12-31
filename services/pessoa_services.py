from models.database import db_session
from models.pessoas import Pessoas


class PessoasServices(Pessoas):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get():
        pessoas = Pessoas.query.all()
        dados_por_pessoa = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        db_session.close()
        return dados_por_pessoa

    def modify(id, nome, idade):
        try:
            pessoa = Pessoas.query.filter_by(id=id).first()
            if pessoa:
                pessoa.nome = nome
                pessoa.idade = idade
                db_session.commit()
                return {'status': 'sucesso', 'mensagem': 'pessoa editada com sucesso.'} 
            db_session.close()
        except Exception:
            {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}

    def save(nome, idade):
        try:
            nova_pessoa = PessoasServices(nome, idade)
            db_session.add(nova_pessoa)
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'pessoa adicionada com sucesso.'}
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}

    def delete(id):
        try:
            pessoa_a_deletar = Pessoas.query.filter_by(id=id).first()
            db_session.delete(pessoa_a_deletar)
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'pessoa excluída com sucesso.'}
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}