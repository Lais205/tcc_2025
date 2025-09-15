# Sistema simples de Login (HTML + Flask + MySQL)

Esse projeto é o MVP para a primeira entrega da disciplina de Projeto de Software:
um sistema simples de **cadastro** e **login** de usuários usando HTML no front,
Flask (Python) no backend e MySQL no banco.

## Estrutura
```
sistema_login/
├─ app.py
├─ requirements.txt
├─ frontend/
│  ├─ index.html
│  ├─ cadastro.html
│  └─ login.html
└─ database/
   └─ script.sql
```

## Passo-a-passo para rodar (rápido)
1. **Instale** Python 3.8+ e o MySQL Server na sua máquina.
2. **Descompacte** este ZIP e abra um terminal na pasta `sistema_login`.
3. **Crie o banco**: rode (substitua `root` e/ou senha se necessário):
   ```
   mysql -u root -p < database/script.sql
   ```
   ou abra o MySQL Workbench e execute o conteúdo do arquivo `database/script.sql`.
4. **Ajuste as credenciais** (se necessário) em `app.py` dentro da variável `DB_CONFIG`:
   - `host`, `user`, `password`, `database`
5. **Criar e ativar um ambiente virtual (opcional, recomendado)**:
   - Linux / macOS:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows (cmd):
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
6. **Instalar dependências**:
   ```
   pip install -r requirements.txt
   ```
7. **Executar o backend**:
   ```
   python app.py
   ```
   O servidor rodará em `http://127.0.0.1:5000/`.
8. **Abrir a aplicação**:
   - Abra o navegador e acesse `http://127.0.0.1:5000/`.
   - Use as páginas de **Cadastro** e **Login**.
9. **Testes rápidos**:
   - Cadastre um usuário pelo formulário.
   - Faça login com o usuário cadastrado.

## Observações
- Os dados de senha são armazenados com hash (werkzeug).
- Para produção, não use `debug=True` e configure corretamente o servidor e as credenciais.
- Se o navegador acusar erro de CORS ou se você preferir, rode apenas o Flask (ele serve o frontend) usando `python app.py` e acesse `http://127.0.0.1:5000/`.
- Em caso de erro de conexão ao MySQL, verifique se o serviço do MySQL está ativo e as credenciais em `app.py`.

Boa entrega! Se quiser eu monto também um vídeo curto (gravação de tela) explicando como demonstrar essa funcionalidade.  
