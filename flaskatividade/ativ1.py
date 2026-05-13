from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    texto = """
    Um decorator (decorador) é uma função que recebe outra função como argumento, 
    adiciona alguma funcionalidade a ela e retorna uma nova função, tudo isso sem 
    modificar o código-fonte da função original.
    Eles servem para reutilizar código, adicionar logs, realizar verificação de 
    autorização, medir tempo de execução ou modificar o comportamento de funções e 
    métodos de forma elegante e limpa (usando o símbolo <code>@</code>).
    No Flask, o decorator <code>@app.route('/')</code> é fundamental. Ele "decora" 
    uma função de visualização (view function) para dizer ao Flask: <em>"Quando o usuário 
    acessar este caminho URL, execute esta função"</em>.
    """
    return texto

@app.route('/curriculo')
def exibir_curriculo():
    curriculo = '''
        <h1>Lucas Emilio Larcher</h1>
        <p><strong>E-mail:</strong>lucasemiliolarcher@gmail.com</p>
        <p><strong>telefone:</strong>(99)99999-9999
        <p><strong>endereço></strong>Rua xxxxxxx xxx, Ap. xxx, xxxxxxxx </p>
        
        <h2>Habilidades</h2>
        <p>Python, Flask, HTML, SQL</p>

        <h2>Formação:</h2>
            <li>Série: 3º ano do Ensino Médio</li>
            <li>Colégio: Cotemig, Unidade Barroca</li>
            <li>Turno: Manhã</li>

        <h2>Objetivos:</h2>
        <li>Melhorar as minhas habilidades de programação</li>
        <li>Ganhar experiência em ambientes de trabalho</li>

        <h2>Conhecimento/Habilidades:</h2>
        <li>Conhecimento sobre hardware e software</li>
        <li>Formatação de computadores</li>
        <li>Instalar e configurar o sistema operacional Windows</li>
        <li>Aplicativos Office: Powerpoint, Word e Excel</li>
        <li>Linguagens de programação: C#, Html, python (em aprendizado),php (em aprendizado), banco de dados (em aprendizado)</li>
        <li>Criação de design e edição de imagens</li>
        <li>Domínio de ferramentas Google</li>

    '''

    return curriculo

if __name__ == "__main__":
    app.run(debug=True)